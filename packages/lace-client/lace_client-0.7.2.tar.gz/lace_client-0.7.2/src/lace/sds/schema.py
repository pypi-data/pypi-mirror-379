"""
EU SDS Schema v1 - Exact mapping to Commission template.
CRITICAL: Preserve exact template wording including typos/spacing.
"""

from enum import Enum
from typing import Dict, List, Optional, Literal, Any
from dataclasses import dataclass, field
from datetime import datetime

# Provenance tracking for every field
Provenance = Literal[
    "dataset",          # Derived from analyzer stats
    "ai_on_stats",      # AI filled using stats-only
    "ai_on_snips",      # AI filled using stats+snippets  
    "user",             # Raw user entry
    "ai_rewrite_user",  # User entry lightly rewritten by AI
    "unknown"           # Could not determine
]

# Exact template bins - preserve typos/spacing
class TextSizeBin(str, Enum):
    LESS_THAN_1B = "Less than 1 billion tokens"
    ONE_B_TO_10T = "1billion to 10 trillions tokens"  # Exact template typo
    MORE_THAN_10T = "More than 10 trillions tokens"
    CUSTOM = "custom"
    
class ImageSizeBin(str, Enum):
    LESS_THAN_1M = "Less than 1 million images"
    ONE_M_TO_1B = "1Million to1 billion images"  # Exact template spacing
    MORE_THAN_1B = "More than 1 billion images"
    CUSTOM = "custom"

class AudioSizeBin(str, Enum):
    LESS_THAN_10K = "Less than 10 000 hours"
    TEN_K_TO_1M = "10 000 to1 million hours"  # Exact template spacing
    MORE_THAN_1M = "More than 1 million hours"
    CUSTOM = "custom"

class VideoSizeBin(str, Enum):
    LESS_THAN_10K = "Less than 10 000 hours"
    TEN_K_TO_1M = "10 000 to1 million hours"  # Exact template spacing
    MORE_THAN_1M = "More than 1 million hours"
    CUSTOM = "custom"


@dataclass
class ProvenancedField:
    """Field with provenance tracking."""
    value: Any
    provenance: Provenance = "unknown"


@dataclass
class Provider:
    """Section 1.1 Provider identification."""
    name: str
    contact: str
    provenance: Provenance = "user"


@dataclass
class AuthorizedRep:
    """Authorized representative (Article 54)."""
    applicable: bool = False
    name: Optional[str] = None
    contact: Optional[str] = None
    provenance: Provenance = "user"


@dataclass  
class ModelInfo:
    """Section 1.2 Model identification."""
    name: str
    version: str
    links: List[str] = field(default_factory=list)
    provenance: Provenance = "user"


@dataclass
class ModelDependency:
    """Model dependencies for fine-tuned models."""
    name: str
    version: str
    summary_link: Optional[str] = None
    provenance: Provenance = "user"


@dataclass
class ModalityInfo:
    """Training data modality information."""
    present: bool = False
    size_bin: Optional[str] = None  # One of the exact bin labels
    custom_size_note: Optional[str] = None
    types_desc: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class DataSourcePublic:
    """Section 2.1 Publicly available datasets."""
    used: bool = False
    modalities: List[str] = field(default_factory=list)
    large_list: List[Dict[str, str]] = field(default_factory=list)  # name, link, parts_used_desc
    other_desc: Optional[str] = None
    additional: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class DataSourcePrivateLicensed:
    """Section 2.2.1 Commercially licensed datasets."""
    used: bool = False
    modalities: List[str] = field(default_factory=list)
    details_desc: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class DataSourcePrivateOther:
    """Section 2.2.2 Private datasets from other third parties."""
    used: bool = False
    modalities: List[str] = field(default_factory=list)
    known_list: List[Dict[str, str]] = field(default_factory=list)  # name, link
    unknown_desc: Optional[str] = None
    additional: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class DataSourceCrawled:
    """Section 2.3 Crawled/scraped data."""
    used: bool = False
    crawler_names: List[str] = field(default_factory=list)
    purposes: Optional[str] = None
    behavior: Optional[str] = None
    period_from: Optional[str] = None  # MM/YYYY
    period_to: Optional[str] = None    # MM/YYYY
    content_desc: Optional[str] = None
    modalities: List[str] = field(default_factory=list)
    top_domains_list_ref: Optional[str] = None  # Path to CSV file
    additional: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class DataSourceUser:
    """Section 2.4 User data."""
    model_interactions_used: bool = False
    other_services_used: bool = False
    services_desc: Optional[str] = None
    modalities: List[str] = field(default_factory=list)
    additional: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class DataSourceSynthetic:
    """Section 2.5 Synthetic data."""
    used: bool = False
    modalities: List[str] = field(default_factory=list)
    market_models: List[Dict[str, str]] = field(default_factory=list)  # name, summary_link
    other_models_desc: Optional[str] = None
    additional: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class DataSourceOther:
    """Section 2.6 Other sources."""
    used: bool = False
    desc: Optional[str] = None
    additional: Optional[str] = None
    provenance: Provenance = "unknown"


@dataclass
class TDMReservations:
    """Section 3.1 TDM reservations."""
    code_of_practice_signatory: bool = False
    measures_desc: Optional[str] = None
    additional: Optional[str] = None
    provenance: Provenance = "user"


@dataclass
class GenerationInfo:
    """Metadata about SDS generation."""
    ai_mode: Literal["local", "cloud", "none"] = "none"
    ai_input: Literal["stats", "stats+snips", "none"] = "none"
    snippet_bytes_sent: int = 0
    dataset_fingerprint: Optional[str] = None
    sampling_seed: Optional[str] = None
    ai_provider: Optional[str] = None
    model_name: Optional[str] = None
    prompt_hash: Optional[str] = None
    tool_version: str = "0.7.0"
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())


@dataclass
class EUSDSSchema:
    """EU AI Act Sufficiently Detailed Summary v1 schema."""
    
    # Metadata
    schema_version: str = "eu_sds.v1"
    version_of_summary: str = "1.0"
    last_update: str = field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d"))
    
    # Section 1: General information
    provider: Provider = field(default_factory=Provider)
    authorized_rep: AuthorizedRep = field(default_factory=AuthorizedRep)
    
    # Section 1.2: Model identification
    model_names: List[ModelInfo] = field(default_factory=list)
    dependencies: List[ModelDependency] = field(default_factory=list)
    date_placed_on_market: Optional[str] = None  # YYYY-MM-DD or YYYY-MM
    date_placed_provenance: Provenance = "user"
    
    # Section 1.3: Modalities and characteristics
    modalities: Dict[str, ModalityInfo] = field(default_factory=lambda: {
        "text": ModalityInfo(),
        "image": ModalityInfo(),
        "audio": ModalityInfo(),
        "video": ModalityInfo(),
        "other": []  # List of custom modalities
    })
    
    latest_data_acquisition: Optional[str] = None  # MM/YYYY
    continuous_after: bool = False
    latest_data_provenance: Provenance = "unknown"
    
    languages_desc: Optional[str] = None
    languages_provenance: Provenance = "unknown"
    
    other_characteristics: Optional[str] = None
    other_char_provenance: Provenance = "unknown"
    
    additional_comments: Optional[str] = None
    additional_provenance: Provenance = "user"
    
    # Section 2: Data sources
    data_sources: Dict[str, Any] = field(default_factory=lambda: {
        "public": DataSourcePublic(),
        "private_licensed": DataSourcePrivateLicensed(),
        "private_other": DataSourcePrivateOther(),
        "crawled": DataSourceCrawled(),
        "user_data": DataSourceUser(),
        "synthetic": DataSourceSynthetic(),
        "other": DataSourceOther()
    })
    
    # Section 3: Data processing
    tdm_reservations: TDMReservations = field(default_factory=TDMReservations)
    illegal_content_removal: Optional[str] = None
    illegal_content_provenance: Provenance = "user"
    other_processing_info: Optional[str] = None
    other_processing_provenance: Provenance = "user"
    
    # Generation metadata
    generation_info: GenerationInfo = field(default_factory=GenerationInfo)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to JSON-serializable dict."""
        def serialize(obj):
            if hasattr(obj, '__dict__'):
                result = {}
                for key, value in obj.__dict__.items():
                    if isinstance(value, (list, dict)):
                        result[key] = serialize(value)
                    elif hasattr(value, '__dict__'):
                        result[key] = serialize(value)
                    elif isinstance(value, Enum):
                        result[key] = value.value
                    else:
                        result[key] = value
                return result
            elif isinstance(obj, dict):
                return {k: serialize(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [serialize(item) for item in obj]
            elif isinstance(obj, Enum):
                return obj.value
            else:
                return obj
        
        return serialize(self)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'EUSDSSchema':
        """Create from dict."""
        # TODO: Implement proper deserialization
        instance = cls()
        # Basic field mapping for now
        for key, value in data.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        return instance
    
    def validate(self) -> List[str]:
        """Validate required fields and return list of errors."""
        errors = []
        
        # Required fields
        if not self.provider.name:
            errors.append("Provider name is required")
        if not self.provider.contact:
            errors.append("Provider contact is required")
        if not self.model_names:
            errors.append("At least one model name is required")
        if not self.date_placed_on_market:
            errors.append("Date placed on market is required")
        
        # At least one modality should be present
        has_modality = any(
            m.present for m in [
                self.modalities.get("text", ModalityInfo()),
                self.modalities.get("image", ModalityInfo()),
                self.modalities.get("audio", ModalityInfo()),
                self.modalities.get("video", ModalityInfo())
            ]
        ) or bool(self.modalities.get("other"))
        
        if not has_modality:
            errors.append("At least one training data modality must be specified")
        
        # At least one data source should be used
        has_source = any([
            self.data_sources["public"].used,
            self.data_sources["private_licensed"].used,
            self.data_sources["private_other"].used,
            self.data_sources["crawled"].used,
            self.data_sources["user_data"].model_interactions_used,
            self.data_sources["user_data"].other_services_used,
            self.data_sources["synthetic"].used,
            self.data_sources["other"].used
        ])
        
        if not has_source:
            errors.append("At least one data source must be specified")
        
        return errors