# educode/__init__.py
"""
EduCode - Module interactif pour apprendre Python
Contient 100 exercices progressifs avec correction automatique
"""

__version__ = "1.0.0"
__author__ = "EduCode Team"
__email__ = "contact@educode.dev"

from .core import EduCode, Exercise
from .exercises import get_all_exercises

__all__ = ['EduCode', 'Exercise', 'get_all_exercises']