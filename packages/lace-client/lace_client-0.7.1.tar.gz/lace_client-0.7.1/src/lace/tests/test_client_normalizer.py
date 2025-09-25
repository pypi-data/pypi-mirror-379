#!/usr/bin/env python3
"""
Unit tests for client.py normalizer to ensure local_facts moves to top-level.
"""

import unittest
import json
import sys
from pathlib import Path
from datetime import datetime

# Import from the correct module path
from lace.client import LaceClient


class TestClientNormalizer(unittest.TestCase):
    """Test the _normalize_analyze_payload_for_server method."""
    
    def setUp(self):
        """Set up test client."""
        # Create client without API key since we're only testing normalization
        self.client = LaceClient(api_key="test_key")
    
    def test_local_facts_moves_to_top_level(self):
        """Test that local_facts moves from config to top-level."""
        payload = {
            'manifest': {
                'total_files': 3,
                'total_bytes': 1000,
                'files': [
                    {'hash': 'abc123', 'path': '/test/file.txt', 'size': 100, 'mtime': 1234567890}
                ]
            },
            'config': {
                'tier': 'minimal',
                'ephemeral': False,
                'local_facts': {
                    'tdm_results': {'test': 'data'},
                    'modalities_detected': {'text': True}
                }
            }
        }
        
        normalized = self.client._normalize_analyze_payload_for_server(payload)
        
        # Check that local_facts is at top level
        self.assertIn('local_facts', normalized)
        self.assertEqual(normalized['local_facts']['tdm_results']['test'], 'data')
        
        # Check that local_facts is removed from config
        self.assertNotIn('local_facts', normalized['config'])
        
        # Check that config still has other fields
        self.assertEqual(normalized['config']['tier'], 'minimal')
        self.assertEqual(normalized['config']['ephemeral'], False)
    
    def test_tdm_stats_duplicated_from_tdm_results(self):
        """Test that tdm_stats is created as a copy of tdm_results for compatibility."""
        payload = {
            'manifest': {'total_files': 1, 'total_bytes': 100, 'files': []},
            'config': {
                'local_facts': {
                    'tdm_results': {'statistics': {'total_domains': 5}}
                }
            }
        }
        
        normalized = self.client._normalize_analyze_payload_for_server(payload)
        
        # Check both tdm_results and tdm_stats exist
        self.assertIn('tdm_results', normalized['local_facts'])
        self.assertIn('tdm_stats', normalized['local_facts'])
        
        # Check they have the same content
        self.assertEqual(
            normalized['local_facts']['tdm_results'],
            normalized['local_facts']['tdm_stats']
        )
    
    def test_files_get_relpath_and_iso_mtime(self):
        """Test that files get proper relpath and ISO8601 mtime."""
        payload = {
            'manifest': {
                'total_files': 2,
                'total_bytes': 200,
                'files': [
                    {'hash': 'abc', 'path': '/full/path/file1.txt', 'size': 100, 'mtime': 1234567890},
                    {'hash': 'def', 'path': 'file2.txt', 'size': 100, 'mtime': 1234567891.5}
                ]
            },
            'config': {}
        }
        
        normalized = self.client._normalize_analyze_payload_for_server(payload)
        
        # Check first file
        file1 = normalized['manifest']['files'][0]
        self.assertEqual(file1['relpath'], 'file1.txt')  # Should be just filename
        self.assertEqual(file1['mtime'], '2009-02-13T23:31:30Z')  # ISO8601 format
        
        # Check second file
        file2 = normalized['manifest']['files'][1]
        self.assertEqual(file2['relpath'], 'file2.txt')
        self.assertEqual(file2['mtime'], '2009-02-13T23:31:31Z')  # Rounded from float
    
    def test_client_info_added(self):
        """Test that client info is added to payload."""
        payload = {
            'manifest': {'total_files': 0, 'total_bytes': 0, 'files': []},
            'config': {}
        }
        
        normalized = self.client._normalize_analyze_payload_for_server(payload)
        
        # Check client info exists
        self.assertIn('client', normalized)
        self.assertEqual(normalized['client']['name'], 'lace-cli')
        self.assertIn('version', normalized['client'])
        self.assertIn('platform', normalized['client'])
    
    def test_existing_client_info_preserved(self):
        """Test that existing client info is not overwritten."""
        payload = {
            'manifest': {'total_files': 0, 'total_bytes': 0, 'files': []},
            'config': {},
            'client': {
                'name': 'custom-client',
                'version': '9.9.9',
                'platform': 'custom'
            }
        }
        
        normalized = self.client._normalize_analyze_payload_for_server(payload)
        
        # Check client info preserved
        self.assertEqual(normalized['client']['name'], 'custom-client')
        self.assertEqual(normalized['client']['version'], '9.9.9')
        self.assertEqual(normalized['client']['platform'], 'custom')
    
    def test_no_local_facts_in_config(self):
        """Test normalization when no local_facts in config."""
        payload = {
            'manifest': {'total_files': 0, 'total_bytes': 0, 'files': []},
            'config': {'tier': 'full', 'ephemeral': True}
        }
        
        normalized = self.client._normalize_analyze_payload_for_server(payload)
        
        # Should not have local_facts at top level if not provided
        self.assertNotIn('local_facts', normalized)
        
        # Config should remain unchanged
        self.assertEqual(normalized['config']['tier'], 'full')
        self.assertEqual(normalized['config']['ephemeral'], True)
    
    def test_deepcopy_prevents_mutation(self):
        """Test that original payload is not mutated."""
        original_payload = {
            'manifest': {
                'total_files': 1,
                'total_bytes': 100,
                'files': [{'hash': 'abc', 'path': 'test.txt', 'size': 100, 'mtime': 1234567890}]
            },
            'config': {
                'tier': 'minimal',
                'local_facts': {'test': 'data'}
            }
        }
        
        # Make a copy to compare later
        import copy
        payload_copy = copy.deepcopy(original_payload)
        
        # Normalize
        normalized = self.client._normalize_analyze_payload_for_server(original_payload)
        
        # Check original is unchanged
        self.assertEqual(original_payload, payload_copy)
        self.assertIn('local_facts', original_payload['config'])  # Still in config
        
        # Check normalized is different
        self.assertIn('local_facts', normalized)  # At top level
        self.assertNotIn('local_facts', normalized['config'])  # Not in config


if __name__ == '__main__':
    # Run tests
    unittest.main(verbosity=2)