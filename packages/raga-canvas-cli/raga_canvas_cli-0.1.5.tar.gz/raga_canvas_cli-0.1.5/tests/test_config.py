"""Tests for configuration management."""

import pytest
import tempfile
import yaml
from pathlib import Path

from raga_canvas_cli.utils.config import ConfigManager, Profile, CanvasConfig


class TestConfigManager:
    """Test configuration manager."""
    
    def test_profile_creation(self):
        """Test profile creation and serialization."""
        profile = Profile(
            name="test",
            api_base="https://api.test.com",
            token="test-token"
        )
        
        assert profile.name == "test"
        assert profile.api_base == "https://api.test.com"
        assert profile.token == "test-token"
        
        profile_dict = profile.to_dict()
        assert "name" in profile_dict
        assert "api_base" in profile_dict
        assert "token" in profile_dict
    
    def test_canvas_config_creation(self):
        """Test canvas config creation."""
        config = CanvasConfig(
            name="test-project",
            version="1.0",
            default_environment="dev"
        )
        
        assert config.name == "test-project"
        assert config.version == "1.0"
        assert config.default_environment == "dev"
        
        config_dict = config.to_dict()
        assert "name" in config_dict
        assert "version" in config_dict
        assert "default_environment" in config_dict
    
    def test_config_file_operations(self):
        """Test config file save/load operations."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # Create config manager with temporary path
            config_manager = ConfigManager()
            config_manager.config_file = temp_path / ".canvasrc"
            
            # Test empty config
            config = config_manager.load_global_config()
            assert config == {"profiles": {}, "current_profile": None}
            
            # Add a profile
            profile = Profile("test", "https://api.test.com", "token")
            config_manager.add_profile(profile)
            
            # Load config again
            config = config_manager.load_global_config()
            assert "test" in config["profiles"]
            assert config["current_profile"] == "test"
            
            # Get profile
            loaded_profile = config_manager.get_profile("test")
            assert loaded_profile.name == "test"
            assert loaded_profile.api_base == "https://api.test.com"
    
    def test_workspace_config_operations(self):
        """Test workspace config operations."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            config_manager = ConfigManager()
            config_manager.workspace_config = temp_path / "canvas.yaml"
            
            # Test no config
            config = config_manager.load_workspace_config()
            assert config is None
            
            # Save config
            canvas_config = CanvasConfig("test-project", "1.0", "dev")
            config_manager.save_workspace_config(canvas_config)
            
            # Load config
            loaded_config = config_manager.load_workspace_config()
            assert loaded_config.name == "test-project"
            assert loaded_config.version == "1.0"
            assert loaded_config.default_environment == "dev"
    
    def test_environment_config_operations(self):
        """Test environment config operations."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            env_dir = temp_path / "environments"
            env_dir.mkdir()
            
            # Create test environment file
            env_config = {
                "environment": "test",
                "api_base": "https://test-api.com",
                "settings": {"debug": True}
            }
            
            with open(env_dir / "test.yaml", 'w') as f:
                yaml.safe_dump(env_config, f)
            
            # Test loading
            config_manager = ConfigManager()
            # Change to temp directory for relative path resolution
            original_cwd = Path.cwd()
            try:
                import os
                os.chdir(temp_path)
                
                loaded_config = config_manager.load_environment_config("test")
                assert loaded_config["environment"] == "test"
                assert loaded_config["api_base"] == "https://test-api.com"
                assert loaded_config["settings"]["debug"] is True
                
                # Test non-existent environment
                empty_config = config_manager.load_environment_config("nonexistent")
                assert empty_config == {}
                
            finally:
                os.chdir(original_cwd)
