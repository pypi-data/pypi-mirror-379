"""
Head Hunter Job Bot Auth Tool

GUI инструмент для авторизации в HeadHunter API через OAuth.
Позволяет получить токен доступа для работы с API hh.ru.
"""

__version__ = "1.0.3"
__author__ = "HeadHunter Job Bot"
__email__ = "noreply@example.com"

from .main import main as auth_main

__all__ = ["auth_main", "__version__"]