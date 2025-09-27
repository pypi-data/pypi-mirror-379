"""
Configuration management for the email sender package.
"""

import os
from typing import Optional
from dataclasses import dataclass
from pathlib import Path

from .exceptions import ConfigurationError


@dataclass
class GmailConfig:
    """Configuration for Gmail SMTP settings."""
    email: str
    password: str
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587


class ConfigManager:
    """
    Manages configuration for the email sender package.
    
    Handles loading configuration from environment variables,
    config files, or direct parameters.
    """
    
    def __init__(self):
        self._config = None
    
    @classmethod
    def from_env(cls) -> 'ConfigManager':
        """
        Create a ConfigManager using environment variables.
        
        Expected environment variables:
        - GMAIL_EMAIL: Gmail email address
        - GMAIL_PASSWORD: Gmail app password
        - GMAIL_SMTP_SERVER: SMTP server (optional, defaults to smtp.gmail.com)
        - GMAIL_SMTP_PORT: SMTP port (optional, defaults to 587)
        
        Returns:
            ConfigManager: Configured instance
            
        Raises:
            ConfigurationError: If required environment variables are missing
        """
        email = os.getenv('GMAIL_EMAIL')
        password = os.getenv('GMAIL_PASSWORD')
        smtp_server = os.getenv('GMAIL_SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(os.getenv('GMAIL_SMTP_PORT', '587'))
        
        if not email:
            raise ConfigurationError("GMAIL_EMAIL environment variable is required")
        if not password:
            raise ConfigurationError("GMAIL_PASSWORD environment variable is required")
        
        manager = cls()
        manager._config = GmailConfig(
            email=email,
            password=password,
            smtp_server=smtp_server,
            smtp_port=smtp_port
        )
        return manager
    
    @classmethod
    def from_file(cls, config_path: str) -> 'ConfigManager':
        """
        Create a ConfigManager using a configuration file.
        
        The config file should be in the format:
        GMAIL_EMAIL=your.email@gmail.com
        GMAIL_PASSWORD=your_app_password
        
        Args:
            config_path: Path to the configuration file
            
        Returns:
            ConfigManager: Configured instance
            
        Raises:
            ConfigurationError: If config file is invalid or missing required values
        """
        config_file = Path(config_path)
        if not config_file.exists():
            raise ConfigurationError(f"Configuration file not found: {config_path}")
        
        config_vars = {}
        try:
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        config_vars[key.strip()] = value.strip()
        except Exception as e:
            raise ConfigurationError(f"Failed to read config file: {str(e)}")
        
        email = config_vars.get('GMAIL_EMAIL')
        password = config_vars.get('GMAIL_PASSWORD')
        smtp_server = config_vars.get('GMAIL_SMTP_SERVER', 'smtp.gmail.com')
        smtp_port = int(config_vars.get('GMAIL_SMTP_PORT', '587'))
        
        if not email:
            raise ConfigurationError("GMAIL_EMAIL is required in config file")
        if not password:
            raise ConfigurationError("GMAIL_PASSWORD is required in config file")
        
        manager = cls()
        manager._config = GmailConfig(
            email=email,
            password=password,
            smtp_server=smtp_server,
            smtp_port=smtp_port
        )
        return manager
    
    @classmethod
    def from_parameters(cls, email: str, password: str, 
                       smtp_server: str = "smtp.gmail.com", 
                       smtp_port: int = 587) -> 'ConfigManager':
        """
        Create a ConfigManager using direct parameters.
        
        Args:
            email: Gmail email address
            password: Gmail app password
            smtp_server: SMTP server address
            smtp_port: SMTP port number
            
        Returns:
            ConfigManager: Configured instance
        """
        manager = cls()
        manager._config = GmailConfig(
            email=email,
            password=password,
            smtp_server=smtp_server,
            smtp_port=smtp_port
        )
        return manager
    
    @property
    def config(self) -> Optional[GmailConfig]:
        """Get the current configuration."""
        return self._config
    
    def validate(self) -> bool:
        """
        Validate the current configuration.
        
        Returns:
            bool: True if configuration is valid
            
        Raises:
            ConfigurationError: If configuration is invalid
        """
        if not self._config:
            raise ConfigurationError("No configuration loaded")
        
        if not self._config.email:
            raise ConfigurationError("Email is required")
        
        if not self._config.password:
            raise ConfigurationError("Password is required")
        
        if '@' not in self._config.email:
            raise ConfigurationError("Invalid email format")
        
        if not self._config.email.endswith('@gmail.com'):
            raise ConfigurationError("Only Gmail addresses are supported")
        
        return True