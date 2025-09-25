"""
PDF provenance analyzer.
"""

import re
from pathlib import Path
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class PDFAnalyzer:
    """Extracts provenance information from PDFs."""
    
    def extract_origin(self, pdf_path: Path) -> Optional[str]:
        """
        Extract origin URL from PDF metadata or content.
        
        Returns:
            Origin URL if found, None otherwise
        """
        try:
            # Try PyPDF2 if available
            try:
                import PyPDF2
                return self._extract_with_pypdf2(pdf_path)
            except ImportError:
                pass
            
            # Fallback to basic extraction
            return self._extract_basic(pdf_path)
            
        except Exception as e:
            logger.debug(f"Failed to analyze PDF {pdf_path}: {e}")
            return None
    
    def _extract_with_pypdf2(self, pdf_path: Path) -> Optional[str]:
        """Extract metadata using PyPDF2."""
        try:
            import PyPDF2
            
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                
                # Check metadata
                if reader.metadata:
                    # Common metadata fields that might contain URLs
                    for field in ['/Author', '/Creator', '/Producer', '/Subject']:
                        if field in reader.metadata:
                            value = str(reader.metadata[field])
                            # Look for URLs
                            urls = re.findall(r'https?://[^\s]+', value)
                            if urls:
                                return urls[0]
                
                # Check first page for URLs
                if len(reader.pages) > 0:
                    first_page = reader.pages[0]
                    text = first_page.extract_text()[:5000]  # First 5KB
                    
                    # Look for origin patterns
                    patterns = [
                        r'(?:source|from|downloaded from)[:\s]+(\S+)',
                        r'(?:available at|retrieved from)[:\s]+(\S+)',
                        r'https?://[^\s]+',
                    ]
                    
                    for pattern in patterns:
                        matches = re.findall(pattern, text, re.IGNORECASE)
                        if matches:
                            # Clean up URL
                            url = matches[0]
                            if url.startswith('http'):
                                return url.rstrip('.,;:')
        
        except Exception as e:
            logger.debug(f"PyPDF2 extraction failed: {e}")
        
        return None
    
    def _extract_basic(self, pdf_path: Path) -> Optional[str]:
        """Basic extraction by reading raw PDF bytes."""
        try:
            with open(pdf_path, 'rb') as f:
                # Read first 50KB
                content = f.read(51200)
            
            # Convert to string, ignoring errors
            text = content.decode('utf-8', errors='ignore')
            
            # Look for URLs in the raw content
            urls = re.findall(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[/\w.-]*', text)
            
            if urls:
                # Filter out common PDF-related URLs
                filtered = [
                    url for url in urls
                    if not any(skip in url.lower() for skip in [
                        'adobe.com', 'w3.org', 'purl.org', 'ns.adobe.com'
                    ])
                ]
                
                if filtered:
                    return filtered[0]
        
        except Exception as e:
            logger.debug(f"Basic PDF extraction failed: {e}")
        
        return None