"""
Tests for privacy guarantees in IP-protected cloud-only SDS implementation.
Ensures no raw content or paths are sent to the server.
"""

import json
import hashlib
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import pytest

from lace.wizard.analyzer_minimal import MinimalAnalyzer
from lace.wizard.suggest import LocalSuggestor
from lace.config.manager import ConfigManager, build_payload_class
from lace.cloud import LaceCloudAPI


class TestPrivacyGuarantees:
    """Test that privacy guarantees are maintained."""
    
    def test_no_file_paths_sent_by_default(self, tmp_path):
        """Verify dataset paths are replaced with deterministic IDs."""
        # Create test dataset
        dataset_path = tmp_path / "test_dataset"
        dataset_path.mkdir()
        (dataset_path / "file1.txt").write_text("content1")
        (dataset_path / "file2.py").write_text("content2")
        
        # Analyze with minimal analyzer
        analyzer = MinimalAnalyzer({'local_salt': 'test_salt_12345'})
        analysis = analyzer.analyze_minimal([str(dataset_path)])
        
        # Check results
        assert 'datasets' in analysis
        assert len(analysis['datasets']) == 1
        
        dataset = analysis['datasets'][0]
        
        # ID should be deterministic hash, not path
        assert dataset['id'].startswith('ds_')
        assert len(dataset['id']) == 13  # ds_ + 10 hex chars
        assert str(dataset_path) not in json.dumps(analysis)
        assert "test_dataset" not in json.dumps(analysis)
        
        # Verify ID is deterministic
        expected_hash = hashlib.sha256(
            f"{dataset_path.absolute()}\ntest_salt_12345".encode()
        ).hexdigest()[:10]
        assert dataset['id'] == f"ds_{expected_hash}"
    
    def test_no_file_content_in_minimal_mode(self, tmp_path):
        """Verify no file content is included in minimal analysis."""
        # Create test files with sensitive content
        dataset_path = tmp_path / "sensitive_data"
        dataset_path.mkdir()
        
        secret_content = "API_KEY=sk_test_secret123"
        (dataset_path / "config.env").write_text(secret_content)
        (dataset_path / "data.json").write_text('{"password": "super_secret"}')
        
        # Analyze
        analyzer = MinimalAnalyzer({'local_salt': 'test_salt'})
        analysis = analyzer.analyze_minimal([str(dataset_path)])
        
        # Verify no content leaked
        analysis_str = json.dumps(analysis)
        assert secret_content not in analysis_str
        assert "sk_test_secret123" not in analysis_str
        assert "super_secret" not in analysis_str
        assert "password" not in analysis_str
        
        # Should only have stats
        assert analysis['datasets'][0]['files'] == 2
        assert analysis['datasets'][0]['bytes'] > 0
        assert '.env' in analysis['extensions']
        assert '.json' in analysis['extensions']
    
    def test_k_anonymity_applied_to_extensions(self, tmp_path):
        """Verify k-anonymity (k=3) is applied to extension histogram."""
        dataset_path = tmp_path / "test"
        dataset_path.mkdir()
        
        # Create files with varying counts
        for i in range(10):
            (dataset_path / f"file{i}.py").write_text("x")
        for i in range(2):  # Below k-threshold
            (dataset_path / f"file{i}.rs").write_text("x")
        (dataset_path / "single.go").write_text("x")  # Below k-threshold
        
        analyzer = MinimalAnalyzer({'local_salt': 'test'})
        analysis = analyzer.analyze_minimal([str(dataset_path)])
        
        extensions = analysis['extensions']
        
        # .py should be included (count >= 3)
        assert '.py' in extensions
        assert extensions['.py'] == 10
        
        # .rs and .go should be aggregated to 'other'
        assert '.rs' not in extensions
        assert '.go' not in extensions
        assert 'other' in extensions
        assert extensions['other'] == 3  # 2 .rs + 1 .go
    
    def test_evidence_refs_without_content(self, tmp_path):
        """Verify evidence files are referenced but not uploaded."""
        dataset_path = tmp_path / "test"
        dataset_path.mkdir()
        (dataset_path / "data.txt").write_text("test")
        
        analyzer = MinimalAnalyzer({'local_salt': 'test'})
        analysis = analyzer.analyze_minimal([str(dataset_path)])
        
        # Check evidence references
        assert 'evidence_refs' in analysis
        assert 'top_domains_csv' in analysis['evidence_refs']
        
        # Should be local path reference, not content
        ref = analysis['evidence_refs']['top_domains_csv']
        assert ref == "./evidence/eu_sds_top_domains.csv"
        
        # Evidence file should be created locally
        evidence_file = Path("./evidence/eu_sds_top_domains.csv")
        assert evidence_file.exists()
        
        # Clean up
        evidence_file.unlink()
        evidence_file.parent.rmdir()
    
    def test_deterministic_dataset_ids(self, tmp_path):
        """Verify dataset IDs are deterministic across runs."""
        dataset_path = tmp_path / "test"
        dataset_path.mkdir()
        (dataset_path / "file.txt").write_text("content")
        
        salt = "consistent_salt_value"
        
        # First run
        analyzer1 = MinimalAnalyzer({'local_salt': salt})
        analysis1 = analyzer1.analyze_minimal([str(dataset_path)])
        id1 = analysis1['datasets'][0]['id']
        
        # Second run with same salt
        analyzer2 = MinimalAnalyzer({'local_salt': salt})
        analysis2 = analyzer2.analyze_minimal([str(dataset_path)])
        id2 = analysis2['datasets'][0]['id']
        
        # Should be identical
        assert id1 == id2
        
        # Different salt should give different ID
        analyzer3 = MinimalAnalyzer({'local_salt': 'different_salt'})
        analysis3 = analyzer3.analyze_minimal([str(dataset_path)])
        id3 = analysis3['datasets'][0]['id']
        
        assert id3 != id1
    
    def test_enhanced_mode_no_raw_content(self, tmp_path):
        """Verify enhanced mode still sends no raw content."""
        dataset_path = tmp_path / "test"
        dataset_path.mkdir()
        
        # Create files with content
        (dataset_path / "README.md").write_text("# My Project\nThis is sensitive info")
        (dataset_path / "data.json").write_text('{"url": "https://example.com/api"}')
        (dataset_path / "LICENSE").write_text("MIT License...")
        
        # Get suggestions (enhanced mode)
        suggestor = LocalSuggestor()
        suggestions = suggestor.suggest_all([str(dataset_path)])
        
        # Check languages (aggregated, not raw)
        assert 'languages' in suggestions
        assert isinstance(suggestions['languages'], dict)
        assert all(0 <= v <= 1.0 for v in suggestions['languages'].values())
        
        # Check domains (extracted, not raw content)
        assert 'domains' in suggestions
        if suggestions['domains']:
            # Should have domain, not full URL
            assert 'example.com' in suggestions['domains']
            assert 'https://example.com/api' not in str(suggestions)
        
        # Check licenses (just SPDX IDs, not content)
        assert 'licenses' in suggestions
        if suggestions['licenses']:
            assert 'MIT' in suggestions['licenses']
            assert "MIT License..." not in str(suggestions)
        
        # Verify no raw content in suggestions
        suggestions_str = json.dumps(suggestions)
        assert "This is sensitive info" not in suggestions_str
        assert "My Project" not in suggestions_str
    
    def test_consent_exact_payload_class(self):
        """Verify consent is per exact payload class string."""
        config_mgr = ConfigManager()
        
        # Different payload classes
        minimal = build_payload_class('minimal', 'none')
        enhanced_no_domains = build_payload_class('enhanced', 'none')
        enhanced_hashed = build_payload_class('enhanced', 'hashed')
        enhanced_clear = build_payload_class('enhanced', 'clear')
        
        # All should be different
        assert minimal == "analysis.min.v1@with_ext_hist"
        assert enhanced_no_domains == "analysis.enhanced.v1@with_ext_hist"
        assert enhanced_hashed == "analysis.enhanced.v1@with_ext_hist@domains=hashed"
        assert enhanced_clear == "analysis.enhanced.v1@with_ext_hist@domains=clear"
        
        # Consent to one shouldn't apply to others
        config_mgr.save_consent(minimal)
        assert config_mgr.has_consent(minimal)
        assert not config_mgr.has_consent(enhanced_no_domains)
        assert not config_mgr.has_consent(enhanced_hashed)
        assert not config_mgr.has_consent(enhanced_clear)
        
        # Clean up
        config_mgr.clear_consent()
    
    def test_domain_hashing_option(self, tmp_path):
        """Verify domains can be hashed before sending."""
        dataset_path = tmp_path / "test"
        dataset_path.mkdir()
        (dataset_path / "urls.txt").write_text("https://github.com/repo\nhttps://example.com/page")
        
        suggestor = LocalSuggestor()
        suggestions = suggestor.suggest_all([str(dataset_path)])
        
        original_domains = suggestions.get('domains', {})
        
        # Simulate hashing as done in CLI
        hashed_domains = {}
        for domain, count in original_domains.items():
            domain_hash = hashlib.sha256(domain.encode()).hexdigest()[:16]
            hashed_domains[f"domain_{domain_hash}"] = count
        
        # Original domain names should not be in hashed version
        hashed_str = json.dumps(hashed_domains)
        if original_domains:
            assert 'github.com' not in hashed_str
            assert 'example.com' not in hashed_str
        
        # Should have hashed entries
        for hashed_key in hashed_domains:
            assert hashed_key.startswith('domain_')
            assert len(hashed_key) == 23  # domain_ + 16 hex chars
    
    @patch('lace.cloud.api.httpx.Client')
    def test_cloud_api_no_path_leakage(self, mock_client, tmp_path):
        """Verify cloud API calls don't leak paths."""
        dataset_path = tmp_path / "my_secret_project"
        dataset_path.mkdir()
        (dataset_path / "data.txt").write_text("content")
        
        # Analyze
        analyzer = MinimalAnalyzer({'local_salt': 'test'})
        analysis = analyzer.analyze_minimal([str(dataset_path)])
        
        # Mock API calls
        mock_response = Mock()
        mock_response.json.return_value = {
            'questions': [],
            'suggestions': {}
        }
        mock_response.raise_for_status = Mock()
        
        mock_client_instance = Mock()
        mock_client_instance.post.return_value = mock_response
        mock_client.return_value = mock_client_instance
        
        # Call cloud API
        api = LaceCloudAPI(api_key='test_key')
        api.prepare_sds(analysis)
        
        # Check what was sent
        mock_client_instance.post.assert_called_once()
        call_args = mock_client_instance.post.call_args
        sent_data = call_args[1]['json']
        
        # Verify no path leakage
        sent_str = json.dumps(sent_data)
        assert str(dataset_path) not in sent_str
        assert "my_secret_project" not in sent_str
        assert "tmp_path" not in sent_str
    
    def test_windows_path_handling(self):
        """Verify Windows paths are handled correctly."""
        # Simulate Windows path
        win_path = "C:\\Users\\Alice\\Documents\\dataset"
        
        # Mock Path to return Windows-style path
        with patch('pathlib.Path') as mock_path:
            mock_path_instance = Mock()
            mock_path_instance.absolute.return_value = Path(win_path)
            mock_path_instance.__str__.return_value = win_path
            mock_path.return_value = mock_path_instance
            
            analyzer = MinimalAnalyzer({'local_salt': 'test'})
            
            # Generate ID
            dataset_id = analyzer._generate_dataset_id(mock_path_instance)
            
            # Should be deterministic hash
            assert dataset_id.startswith('ds_')
            assert '\\' not in dataset_id
            assert 'C:' not in dataset_id
            assert 'Users' not in dataset_id
    
    def test_symlink_loop_detection(self, tmp_path):
        """Verify symlink loops don't cause infinite recursion."""
        # Create directory with symlink loop
        dir_a = tmp_path / "dir_a"
        dir_b = tmp_path / "dir_b"
        dir_a.mkdir()
        dir_b.mkdir()
        
        (dir_a / "file.txt").write_text("content")
        
        # Create circular symlink (if supported by OS)
        try:
            (dir_b / "link_to_a").symlink_to(dir_a)
            (dir_a / "link_to_b").symlink_to(dir_b)
        except OSError:
            pytest.skip("Symlinks not supported on this system")
        
        # Analyze - should not hang
        analyzer = MinimalAnalyzer({'local_salt': 'test'})
        analysis = analyzer.analyze_minimal([str(tmp_path)])
        
        # Should complete successfully
        assert 'datasets' in analysis
        assert analysis['datasets'][0]['files'] >= 1  # At least the real file
        assert not analysis['includes_symlinks']  # We don't follow symlinks


if __name__ == '__main__':
    pytest.main([__file__, '-v'])