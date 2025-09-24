"""Tests for helper utilities."""

import pytest
from pathlib import Path

from raga_canvas_cli.utils.helpers import (
    validate_name, sanitize_name, truncate_text, 
    format_file_size, is_valid_url, safe_filename,
    deep_merge_dicts, expand_environment_variables
)


class TestHelpers:
    """Test helper functions."""
    
    def test_validate_name(self):
        """Test name validation."""
        assert validate_name("valid-name") is True
        assert validate_name("valid_name") is True
        assert validate_name("validname123") is True
        assert validate_name("invalid name") is False
        assert validate_name("invalid@name") is False
        assert validate_name("") is False
        assert validate_name("a" * 51) is False  # Too long
    
    def test_sanitize_name(self):
        """Test name sanitization."""
        assert sanitize_name("valid name") == "valid-name"
        assert sanitize_name("invalid@#$name") == "invalid-name"
        assert sanitize_name("--multiple--hyphens--") == "multiple-hyphens"
        assert sanitize_name("   leading-trailing   ") == "leading-trailing"
    
    def test_truncate_text(self):
        """Test text truncation."""
        assert truncate_text("short", 10) == "short"
        assert truncate_text("this is a long text", 10) == "this is..."
        assert truncate_text("long text", 10, "..") == "long te.."
    
    def test_format_file_size(self):
        """Test file size formatting."""
        assert format_file_size(0) == "0 B"
        assert format_file_size(1024) == "1.0 KB"
        assert format_file_size(1024 * 1024) == "1.0 MB"
        assert format_file_size(1024 * 1024 * 1024) == "1.0 GB"
    
    def test_is_valid_url(self):
        """Test URL validation."""
        assert is_valid_url("https://example.com") is True
        assert is_valid_url("http://localhost:8080") is True
        assert is_valid_url("https://api.canvas.raga.ai") is True
        assert is_valid_url("not-a-url") is False
        assert is_valid_url("ftp://example.com") is False
    
    def test_safe_filename(self):
        """Test safe filename creation."""
        assert safe_filename("normal-file.txt") == "normal-file.txt"
        assert safe_filename("file with spaces.txt") == "file with spaces.txt"
        assert safe_filename('file<>:"/\\|?*.txt') == "file_________.txt"
        assert safe_filename("   .file.   ") == "file"
    
    def test_deep_merge_dicts(self):
        """Test deep dictionary merging."""
        base = {
            "a": 1,
            "b": {
                "c": 2,
                "d": 3
            }
        }
        
        override = {
            "b": {
                "d": 4,
                "e": 5
            },
            "f": 6
        }
        
        result = deep_merge_dicts(base, override)
        
        assert result["a"] == 1
        assert result["b"]["c"] == 2
        assert result["b"]["d"] == 4
        assert result["b"]["e"] == 5
        assert result["f"] == 6
    
    def test_expand_environment_variables(self):
        """Test environment variable expansion."""
        env_vars = {
            "API_URL": "https://api.example.com",
            "VERSION": "1.0"
        }
        
        text = "Connect to ${API_URL}/v$VERSION"
        result = expand_environment_variables(text, env_vars)
        
        assert result == "Connect to https://api.example.com/v1.0"
        
        # Test missing variable
        text = "Missing ${MISSING_VAR} variable"
        result = expand_environment_variables(text, env_vars)
        assert result == "Missing ${MISSING_VAR} variable"
