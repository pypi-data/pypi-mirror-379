"""
IdeaJar - A simple idea recording tool

Quickly record and manage your inspirational ideas
"""

__version__ = "0.2.0"
__author__ = "ideajar"
__description__ = "💡 A simple CLI tool to capture and store your brilliant ideas in a snap"

# Export main functions
from .main import run, add_idea, list_ideas, search_ideas, count_ideas

__all__ = ['run', 'add_idea', 'list_ideas', 'search_ideas', 'count_ideas']