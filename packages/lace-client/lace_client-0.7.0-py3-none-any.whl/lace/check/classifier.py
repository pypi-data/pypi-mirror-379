"""
Status classifier combining heuristic rules and online signals.
Determines copyright/opt-out status with confidence scoring.
"""

from typing import Dict, Any, List, Optional, Tuple, Union
import logging

logger = logging.getLogger(__name__)


def _as_int(value: Union[str, int, float, None], default: Optional[int] = None) -> Optional[int]:
    """
    Safely convert value to integer.
    
    Args:
        value: Value to convert (str, int, float, or None)
        default: Default value if conversion fails
        
    Returns:
        Integer value or default
    """
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


class StatusClassifier:
    """Classify item status based on combined signals."""
    
    # Status categories
    OPTED_OUT = 'OPTED_OUT'
    PROBABLY_OPTED_OUT = 'PROBABLY_OPTED_OUT'
    COPYRIGHTED = 'COPYRIGHTED'
    PUBLIC_WITH_LICENSE = 'PUBLIC_WITH_LICENSE'
    LICENSED_OK = 'LICENSED_OK'
    UNKNOWN = 'UNKNOWN'
    
    def __init__(self, thresholds: Optional[Dict[str, float]] = None):
        """
        Initialize classifier with confidence thresholds.
        
        Args:
            thresholds: Custom confidence thresholds
        """
        # Default thresholds for classification
        self.thresholds = thresholds or {
            'opted_out_strong': 0.8,      # Strong opt-out signal
            'opted_out_weak': 0.5,        # Weak opt-out signal
            'copyright_strong': 0.7,      # Strong copyright signal
            'license_public': 0.6,        # Public license confidence
        }
        
        # Known public licenses
        self.public_licenses = {
            'CC0', 'CC-BY', 'CC-BY-SA', 'MIT', 'APACHE',
            'BSD', 'GPL', 'LGPL', 'PUBLIC-DOMAIN'
        }
        
        # Known restrictive licenses
        self.restrictive_licenses = {
            'CC-BY-NC', 'CC-BY-ND', 'CC-BY-NC-SA', 'CC-BY-NC-ND',
            'PROPRIETARY', 'ALL-RIGHTS-RESERVED'
        }
        
        # Strong opt-out indicators
        self.optout_indicators = {
            'robots_disallow': 1.0,        # robots.txt disallow
            'noai_directive': 1.0,         # Explicit noai directive
            'tdm_optout': 0.9,             # TDM opt-out
            'noimageai': 0.9,              # No image AI training
            'x_robots_noai': 0.85,         # X-Robots-Tag with noai
            'terms_prohibit': 0.8,         # Terms prohibit AI training
            'dmca_notice': 0.7,            # DMCA notice present
        }
    
    def classify(
        self,
        attribution: Dict[str, Any],
        policy_signals: Optional[Dict[str, Any]] = None,
        gpt_attribution: Optional[Dict[str, Any]] = None,
        allowlist: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Classify item status based on all available signals.
        
        Args:
            attribution: Offline attribution signals
            policy_signals: Online policy signals (robots.txt, etc.)
            gpt_attribution: GPT-5 attribution results
            allowlist: User allowlist overrides
            
        Returns:
            Classification result with status and confidence
        """
        result = {
            'status': self.UNKNOWN,
            'confidence': 0.0,
            'evidence': [],
            'signals': []
        }
        
        # Check allowlist first (highest priority)
        if allowlist:
            override = self._check_allowlist(attribution, allowlist)
            if override:
                result['status'] = self.LICENSED_OK
                result['confidence'] = 1.0
                result['evidence'].append(f"Allowlisted: {override}")
                return result
        
        # Collect all signals
        signals = []
        
        # Process offline attribution
        if attribution:
            offline_signals = self._process_attribution(attribution)
            signals.extend(offline_signals)
        
        # Process online policy signals
        if policy_signals:
            online_signals = self._process_policy(policy_signals)
            signals.extend(online_signals)
        
        # Process GPT attribution
        if gpt_attribution:
            gpt_signals = self._process_gpt(gpt_attribution)
            signals.extend(gpt_signals)
        
        # Classify based on combined signals
        status, confidence, evidence = self._combine_signals(signals)
        
        result['status'] = status
        result['confidence'] = confidence
        result['evidence'] = evidence
        result['signals'] = signals
        
        return result
    
    def _check_allowlist(
        self,
        attribution: Dict[str, Any],
        allowlist: Dict[str, Any]
    ) -> Optional[str]:
        """
        Check if item matches allowlist.
        
        Args:
            attribution: Attribution signals
            allowlist: Allowlist dict with domains/hashes
            
        Returns:
            Match reason or None
        """
        # Check domain allowlist
        if 'domains' in allowlist:
            for domain in attribution.get('domains', []):
                if domain in allowlist['domains']:
                    return f"domain:{domain}"
        
        # Check SHA256 allowlist
        if 'sha256' in allowlist:
            sha = attribution.get('sha256')
            if sha and sha in allowlist['sha256']:
                return f"sha256:{sha[:16]}..."
        
        return None
    
    def _process_attribution(self, attribution: Dict[str, Any]) -> List[Dict]:
        """Process offline attribution signals."""
        signals = []
        
        # Check for public licenses
        for license_name in attribution.get('licenses', []):
            if license_name.upper() in self.public_licenses:
                signals.append({
                    'type': 'license_public',
                    'value': license_name,
                    'confidence': 0.8,
                    'source': 'offline'
                })
            elif license_name.upper() in self.restrictive_licenses:
                signals.append({
                    'type': 'license_restrictive',
                    'value': license_name,
                    'confidence': 0.9,
                    'source': 'offline'
                })
        
        # Check for copyright signals
        if attribution.get('copyright_signals'):
            signals.append({
                'type': 'copyright',
                'value': len(attribution['copyright_signals']),
                'confidence': min(0.5 + 0.1 * len(attribution['copyright_signals']), 0.9),
                'source': 'offline'
            })
        
        # Domain confidence (higher if multiple domains agree)
        domains = attribution.get('domains', [])
        if domains:
            # Get top domain by score if available
            domain_scores = attribution.get('domain_scores', {})
            if domain_scores:
                top_domain = max(domain_scores.items(), key=lambda x: x[1])
                signals.append({
                    'type': 'domain',
                    'value': top_domain[0],
                    'confidence': top_domain[1],
                    'source': 'offline'
                })
            else:
                signals.append({
                    'type': 'domain',
                    'value': domains[0],
                    'confidence': 0.5,
                    'source': 'offline'
                })
        
        return signals
    
    def _process_policy(self, policy: Dict[str, Any]) -> List[Dict]:
        """Process online policy signals."""
        signals = []
        
        # Use optout_strength from policy_signals.py
        if 'optout_strength' in policy:
            strength = policy['optout_strength']
            if strength > 0:
                signals.append({
                    'type': 'policy_optout',
                    'value': strength,
                    'confidence': strength,
                    'source': 'policy',
                    'evidence': policy.get('evidence', [])
                })
        
        # Check robots.txt specifics
        if 'robots_txt' in policy:
            robots = policy['robots_txt']
            if robots.get('has_noai'):
                signals.append({
                    'type': 'robots_noai',
                    'value': True,
                    'confidence': 1.0,
                    'source': 'robots.txt',
                    'evidence': ['robots.txt: noai directive']
                })
            
            if '/' in robots.get('disallow', []):
                signals.append({
                    'type': 'robots_disallow',
                    'value': 'all',
                    'confidence': 0.8,
                    'source': 'robots.txt'
                })
            
            crawl_delay = _as_int(robots.get('crawl_delay'), 0)
            if crawl_delay and crawl_delay > 10:
                signals.append({
                    'type': 'crawl_delay',
                    'value': crawl_delay,
                    'confidence': 0.6,
                    'source': 'robots.txt'
                })
        
        # Check ai-robots.txt
        if 'ai_robots_txt' in policy:
            ai_robots = policy['ai_robots_txt']
            if ai_robots.get('has_noai'):
                signals.append({
                    'type': 'ai_robots_noai',
                    'value': True,
                    'confidence': 1.0,
                    'source': 'ai-robots.txt',
                    'evidence': ['ai-robots.txt: noai directive']
                })
        
        # Check X-Robots-Tag headers
        if 'x_robots' in policy:
            x_robots = policy['x_robots']
            all_tags = x_robots.get('all', [])
            for tag in all_tags:
                if 'noai' in tag.lower():
                    signals.append({
                        'type': 'x_robots_noai',
                        'value': tag,
                        'confidence': 0.85,
                        'source': 'X-Robots-Tag',
                        'evidence': [f'X-Robots-Tag: {tag}']
                    })
        
        return signals
    
    def _canonicalize_domain(self, domain: str) -> str:
        """
        Canonicalize domain using public suffix rules.
        Simplistic implementation - just extract base domain.
        """
        # Remove protocol if present
        domain = domain.lower().strip()
        if '://' in domain:
            domain = domain.split('://', 1)[1]
        
        # Remove path if present
        if '/' in domain:
            domain = domain.split('/', 1)[0]
        
        # Remove port if present
        if ':' in domain:
            domain = domain.split(':', 1)[0]
        
        # Simple PSL logic - keep last 2-3 parts
        parts = domain.split('.')
        if len(parts) > 2:
            # Check for common 2-part TLDs
            if parts[-2] in ['co', 'com', 'net', 'org', 'edu', 'gov', 'ac']:
                # Keep last 3 parts for domains like example.co.uk
                return '.'.join(parts[-3:])
        
        # Default: keep last 2 parts
        if len(parts) >= 2:
            return '.'.join(parts[-2:])
        return domain
    
    def _process_gpt(self, gpt_result: Dict[str, Any]) -> List[Dict]:
        """Process GPT-5 attribution results with domain de-duplication."""
        signals = []
        seen_domains = set()
        
        # Handle both list and dict formats
        sources = []
        if isinstance(gpt_result, list):
            sources = gpt_result
        elif isinstance(gpt_result, dict):
            sources = gpt_result.get('domains', gpt_result.get('gpt_sources', gpt_result.get('top_sources', [])))
        
        for item in sources:
            if isinstance(item, dict) and 'domain' in item:
                # Canonicalize domain to avoid duplicates
                canonical = self._canonicalize_domain(item['domain'])
                
                if canonical not in seen_domains:
                    seen_domains.add(canonical)
                    signals.append({
                        'type': 'gpt_domain',
                        'value': canonical,
                        'confidence': item.get('confidence', 0.5),
                        'source': 'gpt5',
                        'evidence': [item.get('evidence', f"GPT-5: {canonical}")]
                    })
        
        return signals
    
    def _combine_signals(
        self,
        signals: List[Dict]
    ) -> Tuple[str, float, List[str]]:
        """
        Combine all signals to determine final status using weighted fusion.
        
        Args:
            signals: List of all signals
            
        Returns:
            Tuple of (status, confidence, evidence)
        """
        if not signals:
            return self.UNKNOWN, 0.0, ["No signals found"]
        
        # Aggregate signals by category
        policy_optout = 0.0
        gpt_attribution = 0.0
        offline_copyright = 0.0
        public_license = 0.0
        evidence = []
        
        # Collect evidence from all signals
        for signal in signals:
            sig_type = signal['type']
            confidence = signal['confidence']
            
            # Add evidence if present
            if 'evidence' in signal and signal['evidence']:
                if isinstance(signal['evidence'], list):
                    evidence.extend(signal['evidence'])
                else:
                    evidence.append(str(signal['evidence']))
            
            # Policy-based opt-out signals
            if sig_type in ['policy_optout', 'robots_noai', 'ai_robots_noai', 'x_robots_noai', 'robots_disallow']:
                policy_optout = max(policy_optout, confidence)
            
            # GPT attribution confidence
            elif sig_type == 'gpt_domain':
                gpt_attribution = max(gpt_attribution, confidence)
            
            # Offline copyright/license signals
            elif sig_type in ['copyright', 'license_restrictive']:
                offline_copyright = max(offline_copyright, confidence)
            
            # Public license signals
            elif sig_type == 'license_public':
                public_license = max(public_license, confidence)
        
        # Apply weighted fusion formula
        # score = 0.5*policy + 0.3*gpt + 0.2*offline
        fusion_score = (
            0.5 * policy_optout +
            0.3 * gpt_attribution +
            0.2 * offline_copyright
        )
        
        # Determine status based on thresholds and signal types
        
        # OVERRIDE: Check for strong opt-out first (policy ≥ 0.8 forces OPTED_OUT)
        if policy_optout >= 0.8:
            return self.OPTED_OUT, policy_optout, evidence or [f"Strong opt-out signal: {policy_optout:.2f}"]
        
        # Check for probable opt-out (policy ≥ 0.5)
        elif policy_optout >= 0.5:
            return self.PROBABLY_OPTED_OUT, policy_optout, evidence or [f"Weak opt-out signal: {policy_optout:.2f}"]
        
        # Check for public license (overrides copyright if present)
        elif public_license >= self.thresholds['license_public']:
            return self.PUBLIC_WITH_LICENSE, public_license, evidence or ["Public license detected"]
        
        # Check for copyright (strong © without permissive license)
        elif offline_copyright >= self.thresholds['copyright_strong'] and public_license < 0.3:
            return self.COPYRIGHTED, offline_copyright, evidence or ["Copyright notices found"]
        
        # Use fusion score for borderline cases
        elif fusion_score >= 0.5:
            return self.PROBABLY_OPTED_OUT, fusion_score, evidence or [f"Combined signals suggest opt-out: {fusion_score:.2f}"]
        
        else:
            # Default to UNKNOWN with fusion score
            return self.UNKNOWN, fusion_score, evidence or ["Insufficient signals for classification"]
    
    def batch_classify(
        self,
        items: List[Dict[str, Any]],
        policy_cache: Optional[Dict[str, Any]] = None,
        allowlist: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Classify multiple items efficiently.
        
        Args:
            items: List of items with attribution/signals
            policy_cache: Shared policy signal cache by domain
            allowlist: User allowlist
            
        Returns:
            List of classification results
        """
        results = []
        
        for item in items:
            # Get policy signals for item's domains
            policy_signals = None
            if policy_cache and 'domains' in item.get('attribution', {}):
                # Aggregate policy signals for all domains
                combined_policy = {}
                for domain in item['attribution']['domains']:
                    if domain in policy_cache:
                        domain_policy = policy_cache[domain]
                        # Merge signals (take strongest)
                        for key, value in domain_policy.items():
                            if key not in combined_policy:
                                combined_policy[key] = value
                            elif isinstance(value, bool) and value:
                                combined_policy[key] = True
                            elif isinstance(value, (int, float)):
                                combined_policy[key] = max(combined_policy[key], value)
                
                if combined_policy:
                    policy_signals = combined_policy
            
            # Classify item
            classification = self.classify(
                attribution=item.get('attribution', {}),
                policy_signals=policy_signals,
                gpt_attribution=item.get('gpt_attribution'),
                allowlist=allowlist
            )
            
            # Add to results with item ID
            result = {
                'id': item.get('id'),
                'path': item.get('path'),
                **classification
            }
            results.append(result)
        
        return results