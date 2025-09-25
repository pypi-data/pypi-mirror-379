"""
pyweld core module

Contains main classes and functions for repository welding,
configuration handling, and error definitions.
"""

# Core classes and functions

class Welder:
    """
    Main class responsible for welding multiple repositories.
    """
    def __init__(self, config):
        self.config = config

    def weld_all(self):
        """
        Weld all configured repositories into the runtime environment.
        """
        print("Welding all repositories according to config...")

def weld_repositories():
    """
    Weld configured repositories globally.
    """
    print("Welding repositories...")

def unweld_repositories():
    """
    Unweld (remove) all welded repositories from the environment.
    """
    print("Unwelding repositories...")

def get_welded_repos():
    """
    Return a dictionary of currently welded repositories and their status.
    """
    return {}

def is_welded():
    """
    Return True if repositories are currently welded, False otherwise.
    """
    return False

class WeldConfig:
    """
    Configuration class for welding repositories.
    """
    pass

class RepoConfig:
    """
    Configuration for individual repositories.
    """
    pass

def load_weld_config(path):
    """
    Load welding configuration from a given path.
    """
    print(f"Loading weld config from {path}")

def create_default_config(name=None):
    """
    Create a default welding configuration.
    """
    print(f"Creating default weld config for project '{name}'")

def weld():
    """
    Simple API function to weld repositories.
    """
    print("Executing weld()")

def unweld():
    """
    Simple API function to unweld repositories.
    """
    print("Executing unweld()")

# Error classes

class WeldError(Exception):
    """Base exception for pyweld errors."""
    pass

class ConfigError(WeldError):
    """Raised when there is a configuration error."""
    pass

class RepoError(WeldError):
    """Raised on repository-related errors."""
    pass

class ImportError(WeldError):
    """Raised on import-related errors in welded environment."""
    pass

# Export all public API

__all__ = [
    "Welder",
    "weld_repositories",
    "unweld_repositories",
    "get_welded_repos",
    "is_welded",
    "WeldConfig",
    "RepoConfig",
    "load_weld_config",
    "create_default_config",
    "weld",
    "unweld",
    "WeldError",
    "ConfigError",
    "RepoError",
    "ImportError",
]
