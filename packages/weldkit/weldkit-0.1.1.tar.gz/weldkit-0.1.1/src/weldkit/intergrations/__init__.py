"""
pyweld integrations module

Provides integration helpers for various environments and runners.
"""

def run_with_welded_repos():
    """
    Run a command with welded repositories environment enabled.
    """
    print("Running command with welded repositories...")

def create_welded_subprocess():
    """
    Create a subprocess that inherits welded repositories environment.
    """
    print("Creating subprocess with welded repositories...")

__all__ = [
    "run_with_welded_repos",
    "create_welded_subprocess",
]
