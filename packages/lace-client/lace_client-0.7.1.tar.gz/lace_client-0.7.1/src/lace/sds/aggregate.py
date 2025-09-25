"""
Multi-dataset aggregation for EU SDS.
Combines stats from multiple datasets into unified view.
"""

import hashlib
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import Counter, defaultdict


def compute_fingerprint(paths: List[Path], stats: List[Dict]) -> str:
    """
    Compute deterministic fingerprint for dataset collection.
    
    Args:
        paths: List of dataset paths
        stats: List of individual dataset stats
        
    Returns:
        SHA256 hex digest of canonical representation
    """
    hasher = hashlib.sha256()
    
    # Sort paths for determinism
    sorted_paths = sorted(str(p) for p in paths)
    for path in sorted_paths:
        hasher.update(path.encode('utf-8'))
        hasher.update(b'\x00')  # Separator
    
    # Add sizes and file counts
    for stat in sorted(stats, key=lambda s: s.get('locator', '')):
        hasher.update(str(stat.get('bytes', 0)).encode('utf-8'))
        hasher.update(b'\x00')
        hasher.update(str(stat.get('files', 0)).encode('utf-8'))
        hasher.update(b'\x00')
    
    return hasher.hexdigest()


def aggregate_datasets(dataset_stats: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Aggregate multiple dataset analyses into unified stats.
    
    Args:
        dataset_stats: List of individual dataset analysis results
        
    Returns:
        Aggregated statistics with both individual and combined views
    """
    if not dataset_stats:
        return {
            "datasets": [],
            "aggregate": {},
            "fingerprint": ""
        }
    
    # Initialize aggregates
    total_bytes = 0
    total_files = 0
    modality_bytes = defaultdict(int)
    modality_files = defaultdict(int)
    lang_counter = Counter()
    domain_counter = Counter()
    license_hints = set()
    mime_counter = Counter()
    
    # Process each dataset
    for stats in dataset_stats:
        total_bytes += stats.get('bytes', 0)
        total_files += stats.get('files', 0)
        
        # Aggregate modalities
        for modality, info in stats.get('modalities', {}).items():
            if info.get('present', False):
                modality_bytes[modality] += info.get('bytes', 0)
                modality_files[modality] += info.get('files', 0)
        
        # Aggregate languages
        for lang, count in stats.get('lang_hist', {}).items():
            lang_counter[lang] += count
        
        # Aggregate domains (if available)
        for domain, count in stats.get('top_domains', {}).items():
            domain_counter[domain] += count
        
        # Collect license hints
        for hint in stats.get('license_hints', []):
            license_hints.add(hint)
        
        # Aggregate MIME types
        for mime, count in stats.get('mime_types', {}).items():
            mime_counter[mime] += count
    
    # Build aggregate structure
    aggregate = {
        "bytes": total_bytes,
        "files": total_files,
        "modalities": {},
        "lang_hist": dict(lang_counter.most_common(50)),  # Top 50 languages
        "top_domains": dict(domain_counter.most_common(1000)),  # Top 1000 domains
        "license_hints": sorted(list(license_hints)),
        "mime_types": dict(mime_counter.most_common(100)),  # Top 100 MIME types
        "dataset_count": len(dataset_stats)
    }
    
    # Process modalities with size estimation
    for modality in ['text', 'image', 'audio', 'video']:
        if modality in modality_bytes:
            aggregate["modalities"][modality] = {
                "present": True,
                "bytes": modality_bytes[modality],
                "files": modality_files[modality],
                "estimated_units": estimate_units(modality, modality_bytes[modality])
            }
        else:
            aggregate["modalities"][modality] = {
                "present": False,
                "bytes": 0,
                "files": 0
            }
    
    # Other modalities
    other_modalities = set(modality_bytes.keys()) - {'text', 'image', 'audio', 'video'}
    if other_modalities:
        aggregate["modalities"]["other"] = []
        for mod in sorted(other_modalities):
            aggregate["modalities"]["other"].append({
                "name": mod,
                "bytes": modality_bytes[mod],
                "files": modality_files[mod]
            })
    
    # Compute fingerprint
    paths = [Path(s.get('locator', '')) for s in dataset_stats]
    fingerprint = compute_fingerprint(paths, dataset_stats)
    
    return {
        "datasets": dataset_stats,
        "aggregate": aggregate,
        "fingerprint": fingerprint
    }


def estimate_units(modality: str, bytes_count: int) -> Dict[str, Any]:
    """
    Estimate units for a modality based on byte count.
    
    Args:
        modality: Type of data (text, image, audio, video)
        bytes_count: Total bytes
        
    Returns:
        Estimated counts in appropriate units
    """
    if modality == 'text':
        # Rough heuristic: 1 token ≈ 4 bytes (varies by language/tokenizer)
        tokens = bytes_count // 4
        return {
            "tokens": tokens,
            "tokens_display": format_large_number(tokens)
        }
    
    elif modality == 'image':
        # Rough heuristic: average image ≈ 500KB
        images = bytes_count // (500 * 1024)
        return {
            "images": images,
            "images_display": format_large_number(images)
        }
    
    elif modality == 'audio':
        # Rough heuristic: 1 hour ≈ 40MB (compressed)
        hours = bytes_count // (40 * 1024 * 1024)
        return {
            "hours": hours,
            "hours_display": format_large_number(hours)
        }
    
    elif modality == 'video':
        # Rough heuristic: 1 hour ≈ 1GB (compressed)
        hours = bytes_count // (1024 * 1024 * 1024)
        return {
            "hours": hours,
            "hours_display": format_large_number(hours)
        }
    
    return {}


def format_large_number(num: int) -> str:
    """Format large numbers with appropriate units."""
    if num >= 1_000_000_000_000:
        return f"{num / 1_000_000_000_000:.1f}T"
    elif num >= 1_000_000_000:
        return f"{num / 1_000_000_000:.1f}B"
    elif num >= 1_000_000:
        return f"{num / 1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num / 1_000:.1f}K"
    else:
        return str(num)


def suggest_large_datasets(aggregate: Dict, threshold_pct: float = 3.0) -> List[Dict]:
    """
    Suggest datasets that might qualify as 'large' per EU template.
    
    The template defines 'large' as >3% of total for a modality.
    Since we don't know the universe, we use relative share within provided datasets.
    
    Args:
        aggregate: Aggregated dataset statistics
        threshold_pct: Percentage threshold (default 3%)
        
    Returns:
        List of dataset suggestions with rationale
    """
    suggestions = []
    
    if not aggregate.get('datasets'):
        return suggestions
    
    # Check each modality
    for modality in ['text', 'image', 'audio', 'video']:
        modality_total = aggregate['aggregate']['modalities'].get(modality, {}).get('bytes', 0)
        
        if modality_total == 0:
            continue
        
        # Find datasets that exceed threshold for this modality
        for dataset in aggregate['datasets']:
            dataset_modality_bytes = dataset.get('modalities', {}).get(modality, {}).get('bytes', 0)
            
            if dataset_modality_bytes > 0:
                percentage = (dataset_modality_bytes / modality_total) * 100
                
                if percentage >= threshold_pct:
                    suggestions.append({
                        'dataset': dataset.get('locator', 'Unknown'),
                        'modality': modality,
                        'percentage': round(percentage, 1),
                        'rationale': f"Represents {percentage:.1f}% of total {modality} data",
                        'bytes': dataset_modality_bytes
                    })
    
    return sorted(suggestions, key=lambda x: x['percentage'], reverse=True)


def generate_top_domains_csv(domains: Dict[str, int], limit: Optional[int] = None) -> str:
    """
    Generate CSV content for top domains list.
    
    Args:
        domains: Domain counts
        limit: Optional limit on number of domains
        
    Returns:
        CSV content as string
    """
    lines = ["domain,count,rank"]
    
    sorted_domains = sorted(domains.items(), key=lambda x: x[1], reverse=True)
    if limit:
        sorted_domains = sorted_domains[:limit]
    
    for rank, (domain, count) in enumerate(sorted_domains, 1):
        # Escape domain if needed
        domain_escaped = domain.replace('"', '""')
        if ',' in domain_escaped or '"' in domain_escaped:
            domain_escaped = f'"{domain_escaped}"'
        
        lines.append(f"{domain_escaped},{count},{rank}")
    
    return '\n'.join(lines)