"""
Verdict calculation engine for Preflight.
"""

from dataclasses import dataclass
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


@dataclass
class PreflightVerdict:
    """Preflight verdict with rationale."""
    status: str  # allow|suspect|deny|unknown
    confidence: float
    rationale: List[str]


class VerdictEngine:
    """Calculates verdict based on signals and policy."""
    
    def __init__(self, policy_mode: str = 'default'):
        """
        Initialize verdict engine.
        
        Args:
            policy_mode: 'default', 'strict', or 'lenient'
        """
        self.policy_mode = policy_mode
    
    def calculate(self, signals: Dict[str, Any], registry_verified: bool) -> PreflightVerdict:
        """
        Calculate verdict from signals.
        
        Args:
            signals: Signal data from scanner
            registry_verified: Whether registry is verified
            
        Returns:
            PreflightVerdict with status, confidence, and rationale
        """
        rationale = []
        confidence = 0.0
        
        # Check opt-out signals (highest priority)
        opt_out = signals.get('opt_out', {})
        deny_count = opt_out.get('summary', {}).get('deny', 0)
        suspect_count = opt_out.get('summary', {}).get('suspect', 0)
        
        if deny_count > 0:
            # Deny verdict
            rationale.append(f"{deny_count} opt-out domain(s) found")
            
            # Add top domains to rationale
            deny_domains = opt_out.get('deny_domains', [])
            for domain_info in deny_domains[:3]:
                domain = domain_info.get('domain', 'unknown')
                source = domain_info.get('source', 'unknown')
                rationale.append(f"{domain} ({source})")
            
            confidence = 0.95 if registry_verified else 0.85
            return PreflightVerdict('deny', confidence, rationale[:5])
        
        # Check license signals
        license_info = signals.get('license', {})
        license_flags = license_info.get('flags', [])
        noassertion = license_info.get('summary', {}).get('noassertion', 0)
        
        suspect_license = False
        if license_flags:
            for flag in license_flags:
                hint = flag.get('hint', '')
                if any(term in hint.lower() for term in ['non-commercial', 'no-derivatives', 'nc', 'nd']):
                    rationale.append(f"Restrictive license: {hint}")
                    suspect_license = True
                    break
        
        # Check PII signals
        pii = signals.get('pii', {})
        pii_severity = pii.get('severity', 'none')
        
        if pii_severity in ('medium', 'high'):
            rationale.append(f"PII detected (severity: {pii_severity})")
            pii_counts = pii.get('findings', {})
            if pii_counts:
                # Add specific PII types found
                pii_types = [k for k, v in pii_counts.items() if v > 0]
                if pii_types:
                    rationale.append(f"PII types: {', '.join(pii_types[:3])}")
        
        # Apply policy rules
        if self.policy_mode == 'strict':
            # Strict mode: any concern triggers suspect/deny
            if suspect_license or noassertion > 0:
                rationale.append("Strict policy: license concerns")
                confidence = 0.75 if registry_verified else 0.65
                return PreflightVerdict('suspect', confidence, rationale[:5])
            
            if pii_severity != 'none':
                rationale.append("Strict policy: PII present")
                confidence = 0.7 if registry_verified else 0.6
                return PreflightVerdict('suspect', confidence, rationale[:5])
        
        elif self.policy_mode == 'lenient':
            # Lenient mode: only hard blocks trigger deny
            if suspect_count > 5:  # Multiple suspects might indicate issue
                rationale.append(f"{suspect_count} suspect domains")
                confidence = 0.6
                return PreflightVerdict('suspect', confidence, rationale[:5])
        
        else:  # default policy
            # Balanced approach
            concern_count = 0
            
            if suspect_license:
                concern_count += 2
            if noassertion > 5:
                concern_count += 1
                rationale.append(f"{noassertion} files with unclear license")
            if pii_severity == 'medium':
                concern_count += 1
            elif pii_severity == 'high':
                concern_count += 2
            if suspect_count > 0:
                concern_count += 1
                rationale.append(f"{suspect_count} suspect domain(s)")
            
            if concern_count >= 3:
                confidence = 0.7 if registry_verified else 0.6
                return PreflightVerdict('suspect', confidence, rationale[:5])
        
        # Check if we have reasonable coverage
        file_count = signals.get('file_count', 0)
        if file_count == 0:
            return PreflightVerdict('unknown', 0.1, ['No files scanned'])
        
        # If using dev registry, lower confidence
        if not registry_verified:
            rationale.append("Using unverified registry")
            confidence = min(0.7, confidence)
        
        # All checks passed
        if not rationale:
            rationale.append("No concerns found")
            if file_count > 0:
                scanned = signals.get('pii', {}).get('coverage', {}).get('files_scanned', 0)
                rationale.append(f"Scanned {scanned}/{file_count} files")
        
        confidence = 0.85 if registry_verified else 0.65
        return PreflightVerdict('allow', confidence, rationale[:5])