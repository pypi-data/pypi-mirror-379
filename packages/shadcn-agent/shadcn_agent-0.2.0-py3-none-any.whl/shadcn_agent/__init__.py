# shadcn_agent/__init__.py
"""
shadcn-agent: A CLI tool for building composable AI agents with LangGraph
"""

__version__ = "0.2.0"
__author__ = "Aryan Bagale"
__email__ = "aryanbagale22@gmail.com"

# Package-level imports for easier access
from .cli import main

__all__ = ["main"]