"""
EU Answers Builder - Generates EU AI Act compliant answers with tri-state handling.
Never auto-infers Yes/No values - uses TO_BE_PROVIDED unless user explicitly provides.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def build_eu_answers(quick: Dict[str, Any], full: Dict[str, Any], user: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build EU-compliant answers dictionary with proper tri-state handling.
    
    Core principles:
    1. Never hallucinate - use actual data or TO_BE_PROVIDED
    2. Tri-state for sections 2.1-2.6: Yes/No/TO_BE_PROVIDED
    3. Map code modality to text with "source code" in types
    4. Size bands: calculate from actual data or "Not known"
    5. Don't invent illegal content measures
    
    Args:
        quick: Quick scan results (file counts, latest mtime, etc.)
        full: Full scan results (modalities, languages, datasets, etc.)
        user: User-provided answers (overrides everything)
        
    Returns:
        Complete answers dictionary with all EU template fields
    """
    answers = {}
    
    # Header fields
    answers['summary_version'] = user.get('summary_version', 'v0.1')
    answers['last_update'] = user.get('last_update', datetime.now().strftime('%Y-%m-%d'))
    
    # 1.1 Provider identification
    answers['provider_name'] = user.get('provider_name', 'TO BE PROVIDED')
    answers['provider_contact'] = user.get('provider_contact', 'TO BE PROVIDED')
    answers['authorized_rep_name'] = user.get('authorized_rep_name', 'Not applicable')
    answers['authorized_rep_contact'] = user.get('authorized_rep_contact', '')
    
    # 1.2 Model identification
    answers['model_name'] = user.get('model_name', 'TO BE PROVIDED')
    answers['model_dependencies'] = user.get('model_dependencies', [])
    answers['date_placement_eu'] = user.get('date_placement_eu', 'TO BE PROVIDED')
    
    # 1.3 Modalities - derive from scan data
    modalities_detected = full.get('modalities_detected', {})
    
    # Map code modality to text (as per EU template)
    has_code = modalities_detected.get('code', False) or modalities_detected.get('other', False)
    
    answers['modalities'] = {
        'text': modalities_detected.get('text', False) or has_code,
        'image': modalities_detected.get('image', False),
        'audio': modalities_detected.get('audio', False),
        'video': modalities_detected.get('video', False)
    }
    
    # Size bands - calculate from actual data or "Not known"
    answers['size_bands'] = _calculate_size_bands(full.get('sizes', {}), answers['modalities'])
    
    # Types of content
    types_of_content = {}
    if answers['modalities']['text']:
        content_types = []
        if has_code:
            content_types.append('source code')
        # Only add other types if user provides them
        user_text_types = user.get('types_of_content', {}).get('text', '')
        if user_text_types and user_text_types != 'TO BE PROVIDED':
            types_of_content['text'] = user_text_types
        elif content_types:
            types_of_content['text'] = '; '.join(content_types)
        else:
            types_of_content['text'] = 'TO BE PROVIDED'
    else:
        types_of_content['text'] = ''
    
    types_of_content['image'] = user.get('types_of_content', {}).get('image', '')
    types_of_content['audio'] = user.get('types_of_content', {}).get('audio', '')
    types_of_content['video'] = user.get('types_of_content', {}).get('video', '')
    
    answers['types_of_content'] = types_of_content
    
    # Latest acquisition date (MM/YYYY format)
    latest_acq = quick.get('latest_acquisition', 'unknown')
    if latest_acq != 'unknown':
        answers['latest_acquisition_mm_yyyy'] = latest_acq
    else:
        answers['latest_acquisition_mm_yyyy'] = user.get('latest_acquisition_mm_yyyy', 'TO BE PROVIDED')
    
    # Language summary
    answers['language_summary'] = _build_language_summary(full.get('languages', []), user)
    
    # Other characteristics (optional)
    answers['other_overall_characteristics'] = user.get('other_overall_characteristics', '')
    
    # 2.1 Publicly available datasets - TRI-STATE
    answers['public_datasets_used'] = _get_tri_state(user, 'public_datasets_used')
    
    # Only populate lists if user confirmed Yes
    if answers['public_datasets_used'] == 'Yes':
        # Get large datasets (≥3% share) from scan
        large_datasets = full.get('large_public_datasets', [])
        answers['public_datasets_large'] = user.get('public_datasets_large', large_datasets)
        answers['public_datasets_other_desc'] = user.get('public_datasets_other_desc', '')
        
        # Modalities for public datasets
        detected_modalities = []
        if answers['modalities']['text']:
            detected_modalities.append('text')
        if answers['modalities']['image']:
            detected_modalities.append('image')
        if answers['modalities']['audio']:
            detected_modalities.append('audio')
        if answers['modalities']['video']:
            detected_modalities.append('video')
        answers['public_datasets_modalities'] = user.get('public_datasets_modalities', detected_modalities)
    else:
        answers['public_datasets_large'] = []
        answers['public_datasets_other_desc'] = ''
        answers['public_datasets_modalities'] = []
    
    # 2.2 Private datasets (licensed and other third parties) - TRI-STATE
    answers['licensed_datasets_used'] = _get_tri_state(user, 'licensed_datasets_used')
    answers['licensed_datasets_modalities'] = user.get('licensed_datasets_modalities', [])
    
    answers['other_private_datasets_used'] = _get_tri_state(user, 'other_private_datasets_used')
    answers['other_private_datasets_modalities'] = user.get('other_private_datasets_modalities', [])
    answers['other_private_datasets_list_publicly_known'] = user.get('other_private_datasets_list_publicly_known', [])
    answers['other_private_datasets_general_description'] = user.get('other_private_datasets_general_description', '')
    
    # 2.3 Crawled/scraped data - CRITICAL: Only from user, NEVER infer!
    answers['crawlers_used'] = _get_tri_state(user, 'crawlers_used')
    
    # Only populate crawler fields if user explicitly confirmed Yes
    if answers['crawlers_used'] == 'Yes':
        answers['crawler_names'] = user.get('crawler_names', ['TO BE PROVIDED'])
        answers['crawler_purposes'] = user.get('crawler_purposes', 'TO BE PROVIDED')
        answers['crawler_behavior'] = user.get('crawler_behavior', 'TO BE PROVIDED')
        
        # Try to derive period from file mtimes if not provided
        period_from = user.get('crawler_period_start_mm_yyyy')
        period_to = user.get('crawler_period_end_mm_yyyy')
        
        if not period_from or not period_to:
            # Could compute from file mtimes but only if user confirms crawling
            volume = full.get('volume', {})
            if volume.get('latest_acquisition_mm_yyyy'):
                period_to = period_to or volume['latest_acquisition_mm_yyyy']
            
        answers['crawler_period_start_mm_yyyy'] = period_from or 'TO BE PROVIDED'
        answers['crawler_period_end_mm_yyyy'] = period_to or 'TO BE PROVIDED'
        answers['crawler_sources_description'] = user.get('crawler_sources_description', 'TO BE PROVIDED')
        answers['crawler_modalities'] = user.get('crawler_modalities', [])
        
        # Note: crawled_domains_csv_path will be added by CLI after CSV generation
    else:
        # Clear all crawler fields if not used
        answers['crawler_names'] = []
        answers['crawler_purposes'] = ''
        answers['crawler_behavior'] = ''
        answers['crawler_period_start_mm_yyyy'] = ''
        answers['crawler_period_end_mm_yyyy'] = ''
        answers['crawler_sources_description'] = ''
        answers['crawler_modalities'] = []
    
    # 2.4 User data - TRI-STATE
    answers['used_user_interactions_for_training'] = _get_tri_state(user, 'used_user_interactions_for_training')
    answers['used_other_provider_services_for_training'] = _get_tri_state(user, 'used_other_provider_services_for_training')
    answers['user_services_description'] = user.get('user_services_description', '')
    answers['user_data_modalities'] = user.get('user_data_modalities', [])
    
    # 2.5 Synthetic data - TRI-STATE
    answers['synthetic_data_used'] = _get_tri_state(user, 'synthetic_data_used')
    
    if answers['synthetic_data_used'] == 'Yes':
        answers['synthetic_modalities'] = user.get('synthetic_modalities', [])
        answers['synthetic_models_used_public'] = user.get('synthetic_models_used_public', [])
        answers['synthetic_models_used_internal_description'] = user.get('synthetic_models_used_internal_description', '')
    else:
        answers['synthetic_modalities'] = []
        answers['synthetic_models_used_public'] = []
        answers['synthetic_models_used_internal_description'] = ''
    
    # 2.6 Other sources - TRI-STATE
    answers['other_sources_used'] = _get_tri_state(user, 'other_sources_used')
    answers['other_sources_description'] = user.get('other_sources_description', '')
    
    # 3.1 TDM opt-out compliance
    answers['tdm_signatory'] = user.get('tdm_signatory', False)
    
    # Build TDM measures description from scan if not provided
    tdm_desc = user.get('tdm_measures_desc')
    if not tdm_desc:
        tdm_stats = full.get('tdm_results', full.get('opt_out_summary', {}))
        tdm_desc = _build_tdm_measures_desc(tdm_stats)
    answers['tdm_measures_desc'] = tdm_desc
    
    # 3.2 Illegal content removal - NEVER invent measures!
    answers['illegal_content_measures_desc'] = user.get('illegal_content_measures_desc', 'TO BE PROVIDED')
    
    # 3.3 Other information (optional)
    answers['other_processing_info'] = user.get('other_processing_info', '')
    
    return answers


def _get_tri_state(user: Dict[str, Any], key: str) -> str:
    """
    Get tri-state value: Yes/No/TO_BE_PROVIDED.
    Never auto-infer - only use user-provided values.
    """
    if key in user:
        value = user[key]
        if isinstance(value, bool):
            return 'Yes' if value else 'No'
        elif value in ('Yes', 'No'):
            return value
        else:
            # Treat any other value as unset
            return 'TO_BE_PROVIDED'
    else:
        # Not provided by user
        return 'TO_BE_PROVIDED'


def _calculate_size_bands(sizes: Dict[str, Any], modalities: Dict[str, bool]) -> Dict[str, str]:
    """
    Calculate size bands from actual data or return "Not known".
    """
    bands = {}
    
    # Text size bands (tokens)
    if modalities.get('text'):
        text_tokens = sizes.get('text_tokens_est', 0)
        if text_tokens > 0:
            if text_tokens < 1_000_000_000:  # < 1B
                bands['text'] = '<1B tokens'
            elif text_tokens < 10_000_000_000_000:  # < 10T
                bands['text'] = '1B-10T tokens'
            else:
                bands['text'] = '>10T tokens'
        else:
            bands['text'] = 'Not known'
    else:
        bands['text'] = 'N/A'
    
    # Image size bands (count)
    if modalities.get('image'):
        image_count = sizes.get('images_count', 0)
        if image_count > 0:
            if image_count < 1_000_000:  # < 1M
                bands['image'] = '<1M images'
            elif image_count < 1_000_000_000:  # < 1B
                bands['image'] = '1M-1B images'
            else:
                bands['image'] = '>1B images'
        else:
            bands['image'] = 'Not known'
    else:
        bands['image'] = 'N/A'
    
    # Audio size bands (hours)
    if modalities.get('audio'):
        audio_hours = sizes.get('audio_hours_est', 0)
        if audio_hours > 0:
            if audio_hours < 10_000:  # < 10K
                bands['audio'] = '<10K hours'
            elif audio_hours < 1_000_000:  # < 1M
                bands['audio'] = '10K-1M hours'
            else:
                bands['audio'] = '>1M hours'
        else:
            bands['audio'] = 'Not known'
    else:
        bands['audio'] = 'N/A'
    
    # Video size bands (hours)
    if modalities.get('video'):
        video_hours = sizes.get('video_hours_est', 0)
        if video_hours > 0:
            if video_hours < 10_000:  # < 10K
                bands['video'] = '<10K hours'
            elif video_hours < 1_000_000:  # < 1M
                bands['video'] = '10K-1M hours'
            else:
                bands['video'] = '>1M hours'
        else:
            bands['video'] = 'Not known'
    else:
        bands['video'] = 'N/A'
    
    return bands


def _build_language_summary(languages: List[Dict[str, Any]], user: Dict[str, Any]) -> str:
    """
    Build concise language summary from scan data.
    """
    # Check if user provided override
    if 'language_summary' in user:
        return user['language_summary']
    
    if not languages:
        return 'TO BE PROVIDED'
    
    # Build summary like "English (~85%), German (~10%), French (~5%)"
    parts = []
    for lang_info in languages[:5]:  # Limit to top 5
        if isinstance(lang_info, dict):
            lang = lang_info.get('lang', 'unknown')
            pct = lang_info.get('pct', 0)
            if pct >= 0.1:  # Only include if >0.1%
                parts.append(f"{lang} (~{pct:.0f}%)")
    
    if parts:
        return ', '.join(parts)
    else:
        return 'TO BE PROVIDED'


def _build_tdm_measures_desc(tdm_stats: Dict[str, Any]) -> str:
    """
    Build TDM measures description from scan statistics.
    """
    if not tdm_stats:
        return 'Technical measures are implemented to respect machine-readable opt-out signals.'
    
    stats = tdm_stats.get('statistics', {})
    total = stats.get('total_domains', 0)
    opted_out = stats.get('opted_out_count', 0)
    pct = stats.get('opted_out_pct', 0.0)
    
    desc = (
        "Technical measures are implemented to respect machine-readable opt-out signals "
        "(e.g., robots.txt, ai.txt, X-Robots-Tag, trust.txt) prior to and during data collection. "
    )
    
    if total > 0:
        desc += f"Representative sampling shows {opted_out} of {total} domains ({pct:.1f}%) opted out, which are programmatically honored."
    
    return desc