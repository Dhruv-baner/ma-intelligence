
"""
Configuration Loader for M&A Intelligence Platform
Usage: from src.config_loader import load_config
"""
import yaml
import os

def load_config():
    """Load main configuration file"""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def load_data_sources():
    """Load data sources configuration"""
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'data_sources.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def get_database_path():
    """Get database path from config"""
    config = load_config()
    return config['database']['path']

def get_ma_thresholds():
    """Get M&A probability alert thresholds"""
    config = load_config()
    return config['monitoring']['ma_probability_thresholds']

def get_sec_user_agent():
    """Get SEC EDGAR user agent string"""
    data_sources = load_data_sources()
    return data_sources['sec_edgar'].get('user_agent', 'M&A Intelligence Platform')
