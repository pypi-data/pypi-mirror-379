"""
Run tracker integration for W&B, MLflow, etc.
"""

import json
import os
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
import logging

from .utils import redact_sensitive
from .constants import EXIT_NETWORK_ERROR, EXIT_VALIDATION_ERROR

logger = logging.getLogger(__name__)


class RunTrackerConnector:
    """Base class for run tracker connectors."""
    
    def fetch_metadata(self, run_id: str) -> Dict[str, Any]:
        """Fetch metadata from run tracker."""
        raise NotImplementedError
    
    def fetch_artifacts(self, run_id: str, dest_dir: Path) -> Dict[str, Path]:
        """Download artifacts to local directory."""
        raise NotImplementedError
    
    def fetch_preflight(self, run_id: str) -> Optional[Dict[str, Any]]:
        """Fetch preflight report if available."""
        raise NotImplementedError


class WandBConnector(RunTrackerConnector):
    """Weights & Biases connector."""
    
    def __init__(self):
        try:
            import wandb
            self.wandb = wandb
        except ImportError:
            raise ImportError("W&B not installed. Run: pip install wandb")
        
        # Initialize API if not already done
        try:
            # Don't auto-login, use existing credentials
            self.api = self.wandb.Api()
        except Exception as e:
            raise ValueError(f"Failed to initialize W&B API. Ensure WANDB_API_KEY is set: {redact_sensitive(str(e))}")
    
    def parse_run_path(self, run_path: str) -> Tuple[str, str, str]:
        """Parse wandb:entity/project/run format."""
        # Remove wandb: prefix if present
        if run_path.startswith('wandb:'):
            run_path = run_path[6:]
        
        parts = run_path.split('/')
        if len(parts) != 3:
            raise ValueError(
                f"Invalid W&B run path: {run_path}. "
                f"Expected format: wandb:entity/project/run_id or entity/project/run_id"
            )
        return parts[0], parts[1], parts[2]
    
    def fetch_metadata(self, run_path: str) -> Dict[str, Any]:
        """Fetch metadata from W&B run."""
        entity, project, run_id = self.parse_run_path(run_path)
        
        try:
            run = self.api.run(f"{entity}/{project}/{run_id}")
            
            # Extract key metadata
            metadata = {
                'run_id': run_id,
                'entity': entity,
                'project': project,
                'name': run.name,
                'state': run.state,
                'config': dict(run.config),
                'summary': dict(run.summary),
                'tags': run.tags,
                'created_at': run.created_at,
                'url': run.url,
            }
            
            # Look for dataset information in config
            config = run.config
            
            # Common patterns for dataset info
            dataset_info = {}
            for key in ['dataset', 'data', 'train_dataset', 'dataset_name', 'dataset_path']:
                if key in config:
                    dataset_info[key] = config[key]
            
            # Look for model information
            model_info = {}
            for key in ['model', 'model_name', 'architecture', 'model_type', 'base_model']:
                if key in config:
                    model_info[key] = config[key]
            
            # Look for training info
            training_info = {}
            for key in ['epochs', 'batch_size', 'learning_rate', 'optimizer', 'loss']:
                if key in config:
                    training_info[key] = config[key]
                elif key in run.summary:
                    training_info[key] = run.summary[key]
            
            metadata['dataset_info'] = dataset_info
            metadata['model_info'] = model_info
            metadata['training_info'] = training_info
            
            return metadata
            
        except Exception as e:
            error_msg = redact_sensitive(str(e))
            if 'not found' in error_msg.lower():
                raise ValueError(f"W&B run not found or not accessible: {run_path}")
            elif 'permission' in error_msg.lower() or 'unauthorized' in error_msg.lower():
                raise ValueError(f"Permission denied for W&B run: {run_path}. Check WANDB_API_KEY and run visibility.")
            else:
                raise RuntimeError(f"Failed to fetch W&B metadata: {error_msg}")
    
    def fetch_artifacts(self, run_path: str, dest_dir: Path) -> Dict[str, Path]:
        """Download artifacts from W&B run."""
        entity, project, run_id = self.parse_run_path(run_path)
        
        try:
            run = self.api.run(f"{entity}/{project}/{run_id}")
            
            artifacts = {}
            
            # Download logged artifacts
            for artifact in run.logged_artifacts():
                artifact_dir = dest_dir / artifact.name
                artifact_dir.mkdir(parents=True, exist_ok=True)
                
                # Download artifact
                artifact.download(str(artifact_dir))
                artifacts[artifact.name] = artifact_dir
                
                logger.debug(f"Downloaded artifact: {artifact.name}")
            
            # Also look for files in the run
            for file in run.files():
                if file.name.endswith(('.json', '.yaml', '.yml', '.txt', '.md')):
                    file_path = dest_dir / file.name
                    file_path.parent.mkdir(parents=True, exist_ok=True)
                    file.download(str(file_path))
                    artifacts[file.name] = file_path
                    
                    logger.debug(f"Downloaded file: {file.name}")
            
            return artifacts
            
        except Exception as e:
            error_msg = redact_sensitive(str(e))
            if 'not found' in error_msg.lower():
                logger.warning(f"No artifacts found for run: {run_path}")
                return {}
            else:
                raise RuntimeError(f"Failed to fetch W&B artifacts: {error_msg}")
    
    def fetch_preflight(self, run_path: str) -> Optional[Dict[str, Any]]:
        """Fetch preflight report from W&B run if available."""
        entity, project, run_id = self.parse_run_path(run_path)
        
        try:
            run = self.api.run(f"{entity}/{project}/{run_id}")
            
            # Look for preflight.json in files
            for file in run.files():
                if file.name == 'preflight.json' or file.name.endswith('/preflight.json'):
                    with tempfile.TemporaryDirectory() as tmpdir:
                        file_path = Path(tmpdir) / 'preflight.json'
                        file.download(str(file_path))
                        
                        with open(file_path, 'r') as f:
                            return json.load(f)
            
            # Look in config for preflight data
            if 'preflight' in run.config:
                return run.config['preflight']
            
            # Look in summary
            if 'preflight' in run.summary:
                return run.summary['preflight']
            
            return None
            
        except Exception as e:
            logger.error(f"Failed to fetch preflight from W&B: {redact_sensitive(str(e))}")
            return None


class MLflowConnector(RunTrackerConnector):
    """MLflow connector."""
    
    def __init__(self):
        try:
            import mlflow
            self.mlflow = mlflow
        except ImportError:
            raise ImportError("MLflow not installed. Run: pip install mlflow")
        
        # Check if tracking URI is set
        tracking_uri = os.getenv('MLFLOW_TRACKING_URI')
        if not tracking_uri:
            logger.warning("MLFLOW_TRACKING_URI not set, using default local storage")
    
    def fetch_metadata(self, run_id: str) -> Dict[str, Any]:
        """Fetch metadata from MLflow run."""
        try:
            client = self.mlflow.tracking.MlflowClient()
            run = client.get_run(run_id)
            
            metadata = {
                'run_id': run_id,
                'experiment_id': run.info.experiment_id,
                'status': run.info.status,
                'start_time': run.info.start_time,
                'end_time': run.info.end_time,
                'params': dict(run.data.params),
                'metrics': dict(run.data.metrics),
                'tags': dict(run.data.tags),
            }
            
            # Extract dataset info from params/tags
            dataset_info = {}
            for key, value in run.data.params.items():
                if 'dataset' in key.lower() or 'data' in key.lower():
                    dataset_info[key] = value
            for key, value in run.data.tags.items():
                if 'dataset' in key.lower() or 'data' in key.lower():
                    dataset_info[key] = value
            
            metadata['dataset_info'] = dataset_info
            
            return metadata
            
        except Exception as e:
            error_msg = redact_sensitive(str(e))
            if 'not found' in error_msg.lower():
                raise ValueError(f"MLflow run not found: {run_id}. Check run ID and tracking URI.")
            elif 'permission' in error_msg.lower():
                raise ValueError(f"Permission denied for MLflow run: {run_id}")
            else:
                raise RuntimeError(f"Failed to fetch MLflow metadata: {error_msg}")
    
    def fetch_artifacts(self, run_id: str, dest_dir: Path) -> Dict[str, Path]:
        """Download artifacts from MLflow run."""
        try:
            client = self.mlflow.tracking.MlflowClient()
            
            # Download all artifacts
            artifact_path = client.download_artifacts(run_id, "", dst_path=str(dest_dir))
            
            # Map artifact names to paths
            artifacts = {}
            for root, dirs, files in os.walk(artifact_path):
                for file in files:
                    file_path = Path(root) / file
                    rel_path = file_path.relative_to(artifact_path)
                    artifacts[str(rel_path)] = file_path
            
            return artifacts
            
        except Exception as e:
            error_msg = redact_sensitive(str(e))
            if 'not found' in error_msg.lower():
                logger.warning(f"No artifacts found for MLflow run: {run_id}")
                return {}
            else:
                raise RuntimeError(f"Failed to fetch MLflow artifacts: {error_msg}")
    
    def fetch_preflight(self, run_id: str) -> Optional[Dict[str, Any]]:
        """Fetch preflight report from MLflow run if available."""
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                artifacts = self.fetch_artifacts(run_id, Path(tmpdir))
                
                # Look for preflight.json
                for name, path in artifacts.items():
                    if name == 'preflight.json' or name.endswith('/preflight.json'):
                        with open(path, 'r') as f:
                            return json.load(f)
            
            return None
            
        except Exception as e:
            logger.error(f"Failed to fetch preflight from MLflow: {redact_sensitive(str(e))}")
            return None


def get_connector(tracker_type: str) -> RunTrackerConnector:
    """Get connector for the specified tracker type."""
    if tracker_type == 'wandb':
        return WandBConnector()
    elif tracker_type == 'mlflow':
        return MLflowConnector()
    else:
        raise ValueError(f"Unknown tracker type: {tracker_type}")


def parse_run_reference(reference: str) -> Tuple[str, str]:
    """Parse run reference like wandb:entity/project/run."""
    if ':' not in reference:
        raise ValueError(f"Invalid run reference: {reference}. Expected format: tracker:path")
    
    tracker_type, run_path = reference.split(':', 1)
    return tracker_type, run_path


def fetch_from_run_tracker(reference: str, dest_dir: Optional[Path] = None) -> Dict[str, Any]:
    """
    Fetch metadata and artifacts from run tracker.
    
    Args:
        reference: Run reference like wandb:entity/project/run or mlflow:run_id
        dest_dir: Directory to download artifacts to
    
    Returns:
        Dict with metadata, artifacts, and preflight if available
    
    Raises:
        ImportError: If tracker package not installed
        ValueError: If run not found or not accessible
        RuntimeError: For other fetch errors
    """
    try:
        tracker_type, run_path = parse_run_reference(reference)
    except ValueError as e:
        # Provide helpful error message
        raise ValueError(
            f"Invalid run reference format: {reference}. "
            f"Expected format: wandb:entity/project/run or mlflow:run_id"
        ) from e
    
    # Get connector, handling import errors gracefully
    try:
        connector = get_connector(tracker_type)
    except ImportError as e:
        # Re-raise with helpful message
        if 'wandb' in str(e).lower():
            raise ImportError(
                "W&B not installed. Run: pip install wandb\n"
                "Or use MLflow: mlflow:run_id"
            ) from e
        elif 'mlflow' in str(e).lower():
            raise ImportError(
                "MLflow not installed. Run: pip install mlflow\n"
                "Or use W&B: wandb:entity/project/run"
            ) from e
        else:
            raise
    
    # Create temp dir if not specified
    if dest_dir is None:
        dest_dir = Path(tempfile.mkdtemp(prefix='lace_run_'))
    
    result = {
        'tracker': tracker_type,
        'run_path': run_path,
        'dest_dir': dest_dir,
    }
    
    # Fetch metadata with error handling
    try:
        result['metadata'] = connector.fetch_metadata(run_path)
    except Exception as e:
        logger.warning(f"Failed to fetch metadata: {redact_sensitive(str(e))}")
        result['metadata'] = {}
    
    # Fetch artifacts with error handling
    try:
        result['artifacts'] = connector.fetch_artifacts(run_path, dest_dir)
    except Exception as e:
        logger.warning(f"Failed to fetch artifacts: {redact_sensitive(str(e))}")
        result['artifacts'] = {}
    
    # Fetch preflight (optional)
    try:
        result['preflight'] = connector.fetch_preflight(run_path)
    except Exception as e:
        logger.warning(f"Failed to fetch preflight: {redact_sensitive(str(e))}")
        result['preflight'] = None
    
    # Check if we got anything useful
    if not result['metadata'] and not result['artifacts']:
        raise RuntimeError(
            f"No data retrieved from {tracker_type} run: {run_path}. "
            f"Check that the run exists and you have access."
        )
    
    return result