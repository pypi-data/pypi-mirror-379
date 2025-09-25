#!/usr/bin/env python3
"""
CLI точка входа для head-hunter-job-bot-auth-tool.

Этот модуль предоставляет командную строку для запуска
GUI инструмента авторизации в HeadHunter API.
"""

import sys
import argparse
from . import __version__
from .main import main as auth_main


def print_version():
    """Выводит информацию о версии"""
    print(f"head-hunter-job-bot-auth-tool {__version__}")
    print("GUI инструмент для авторизации в HeadHunter API")


def print_help():
    """Выводит справочную информацию"""
    help_text = f"""
head-hunter-job-bot-auth-tool {__version__}

GUI инструмент для авторизации в HeadHunter API через OAuth.

ИСПОЛЬЗОВАНИЕ:
    head-hunter-job-bot-auth-tool [OPTIONS]

ОПЦИИ:
    -h, --help       Показать эту справку
    -v, --version    Показать версию программы

ОПИСАНИЕ:
    Этот инструмент открывает графический интерфейс для авторизации
    в API HeadHunter.ru через OAuth. После успешной авторизации
    токен доступа будет выведен в консоль в формате JSON.

ТРЕБОВАНИЯ:
    - Python 3.9+
    - PyQt6
    - PyQt6-WebEngine
    - requests

ПРИМЕРЫ:
    # Запуск инструмента авторизации
    head-hunter-job-bot-auth-tool

    # Показать версию
    head-hunter-job-bot-auth-tool --version

    # Показать справку
    head-hunter-job-bot-auth-tool --help

РЕЗУЛЬТАТ:
    После успешной авторизации в консоль будет выведен JSON с токеном:
    {{
        "access_token": "...",
        "refresh_token": "...",
        "access_expires_at": 1234567890
    }}

Сохраните токен в безопасном месте для использования с HeadHunter API.
"""
    print(help_text.strip())


def parse_arguments():
    """Парсит аргументы командной строки"""
    parser = argparse.ArgumentParser(
        prog='head-hunter-job-bot-auth-tool',
        description='GUI инструмент для авторизации в HeadHunter API',
        add_help=False  # Отключаем стандартную справку, чтобы использовать свою
    )
    
    parser.add_argument(
        '-h', '--help',
        action='store_true',
        help='Показать справку'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help='Показать версию'
    )
    
    return parser.parse_args()


def main():
    """Главная функция CLI"""
    try:
        args = parse_arguments()
        
        if args.help:
            print_help()
            return 0
            
        if args.version:
            print_version()
            return 0
        
        # Запускаем основную функцию авторизации
        auth_main()
        return 0
        
    except KeyboardInterrupt:
        print("\n❌ Операция отменена пользователем")
        return 1
    except Exception as e:
        print(f"❗ Ошибка: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())