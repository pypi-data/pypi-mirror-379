#!/usr/bin/env python3
"""
GUI скрипт для авторизации в HH.ru API через веб-интерфейс.

Позволяет получить токен доступа для работы с API hh.ru
через OAuth авторизацию с графическим интерфейсом.
"""

import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import parse_qs, urlencode, urlsplit
from typing import Dict, Any
import io
from contextlib import redirect_stderr

# Подавляем системные логи Qt до импорта
os.environ['QT_LOGGING_RULES'] = '*.debug=false;*.info=false;*.warning=false'
os.environ['QT_LOGGING_TO_CONSOLE'] = '0'
os.environ['QTWEBENGINE_DISABLE_SANDBOX'] = '1'
os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--disable-logging --log-level=3 --disable-gpu-sandbox'


class FilteredStderr:
    """Фильтрует системные сообщения, пропуская только важные"""
    
    def __init__(self, original_stderr):
        self.original_stderr = original_stderr
        self.buffer = ""
    
    def write(self, text):
        # Фильтруем известные системные сообщения
        if any(pattern in text for pattern in [
            "AVCaptureDeviceType",
            "QtWebEngineProcess",
            "WARNING:",
            "Continuity Camera"
        ]):
            return  # Игнорируем
        
        # Пропускаем наши сообщения
        self.original_stderr.write(text)
    
    def flush(self):
        self.original_stderr.flush()


def check_dependencies():
    """Проверяет наличие необходимых зависимостей"""
    try:
        import requests
    except ImportError:
        print("❗ Ошибка: Требуется установить библиотеку requests")
        print("Установите зависимости: pip install requests")
        sys.exit(1)

    try:
        from PyQt6.QtCore import QUrl
        from PyQt6.QtWidgets import QApplication, QMainWindow
        from PyQt6.QtWebEngineCore import QWebEngineUrlSchemeHandler, QWebEngineUrlScheme
        from PyQt6.QtWebEngineWidgets import QWebEngineView
    except ImportError:
        print("❗ Ошибка: PyQt6 не найден!")
        print("Установите PyQt6 для использования GUI авторизации:")
        print("pip install PyQt6 PyQt6-WebEngine")
        sys.exit(1)

    return True


# Константы для Android клиента HH.ru
ANDROID_CLIENT_ID = "HIOMIAS39CA9DICTA7JIO64LQKQJF5AGIK74G9ITJKLNEDAOH5FHS5G1JI7FOEGD"
ANDROID_CLIENT_SECRET = "V9M870DE342BGHFRUJ5FTCGCUA1482AN0DI8C5TFI9ULMA89H10N60NOP8I4JMVS"

# OAuth настройки
OAUTH_BASE_URL = "https://hh.ru/oauth"
REDIRECT_URI = ""  # Пустой redirect_uri
SCOPE = ""
STATE = ""


class SimpleOAuthClient:
    """Простой OAuth клиент для HH.ru API"""
    
    def __init__(self):
        self.client_id = ANDROID_CLIENT_ID
        self.client_secret = ANDROID_CLIENT_SECRET
        self.redirect_uri = REDIRECT_URI
        self.scope = SCOPE
        self.state = STATE
        
        # Импортируем requests только после проверки зависимостей
        import requests
        self.session = requests.Session()
        
    @property
    def authorize_url(self) -> str:
        """Генерирует URL для авторизации"""
        params = {
            'client_id': self.client_id,
            'response_type': 'code',
        }
        # Добавляем redirect_uri только если он не пустой
        if self.redirect_uri:
            params['redirect_uri'] = self.redirect_uri
        # Добавляем scope и state только если они не пустые
        if self.scope:
            params['scope'] = self.scope
        if self.state:
            params['state'] = self.state
            
        params_qs = urlencode(params)
        return f"{OAUTH_BASE_URL}/authorize?{params_qs}"
    
    def authenticate(self, code: str) -> Dict[str, Any]:
        """Обменивает код авторизации на токен доступа"""
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code,
            'grant_type': 'authorization_code',
            # Не добавляем redirect_uri в запрос токена
        }
        
        response = self.session.post(f"{OAUTH_BASE_URL}/token", data=params)
        if response.status_code != 200:
            raise Exception(f"Ошибка получения токена: {response.status_code} {response.text}")
            
        token_data = response.json()
        
        return {
            'access_token': token_data.get('access_token'),
            'refresh_token': token_data.get('refresh_token'),
            'access_expires_at': int(time.time()) + token_data.get('expires_in', 0),
        }


class HHAndroidUrlSchemeHandler:
    """Обработчик кастомной URL схемы hhandroid://"""
    
    def __init__(self, parent: "WebViewWindow"):
        # Импортируем PyQt6 только после проверки зависимостей
        from PyQt6.QtWebEngineCore import QWebEngineUrlSchemeHandler
        
        # Вызываем конструктор правильного базового класса
        QWebEngineUrlSchemeHandler.__init__(self)
        self.parent = parent

    def requestStarted(self, info) -> None:
        url = info.requestUrl().toString()
        if url.startswith("hhandroid://"):
            self.parent.handle_redirect_uri(url)


class WebViewWindow:
    """Окно с веб-браузером для авторизации"""
    
    def __init__(self, oauth_client: SimpleOAuthClient):
        # Импортируем PyQt6 только после проверки зависимостей
        from PyQt6.QtCore import QUrl
        from PyQt6.QtWidgets import QMainWindow
        from PyQt6.QtWebEngineCore import QWebEngineUrlSchemeHandler
        from PyQt6.QtWebEngineWidgets import QWebEngineView
        
        # Создаем объект QMainWindow
        self.main_window = QMainWindow()
        self.oauth_client = oauth_client
        self.oauth_client = oauth_client
        
        # Настройка WebEngineView
        self.web_view = QWebEngineView()
        self.main_window.setCentralWidget(self.web_view)
        self.main_window.setWindowTitle("Авторизация на HH.RU")
        
        # Обработчик кастомной схемы
        self.hhandroid_handler = HHAndroidUrlSchemeHandler(self)
        profile = self.web_view.page().profile()
        profile.installUrlSchemeHandler(b"hhandroid", self.hhandroid_handler)
        
        # Настройки окна для мобильного вида
        self.main_window.resize(480, 800)
        self.web_view.setUrl(QUrl(oauth_client.authorize_url))

    def handle_redirect_uri(self, redirect_uri: str) -> None:
        """Обрабатывает redirect URI с кодом авторизации"""
        sp = urlsplit(redirect_uri)
        code = parse_qs(sp.query).get("code", [None])[0]
        
        if code:
            try:
                token = self.oauth_client.authenticate(code)
                print("🔓 Авторизация прошла успешно!")
                print("💾 Полученный токен:")
                print(json.dumps(token, ensure_ascii=False, indent=2))
                self.main_window.close()
            except Exception as e:
                print(f"❗ Ошибка при получении токена: {e}")
        else:
            print("❗ Не удалось получить код авторизации")


def main():
    """Главная функция"""
    print("🚀 HH.ru GUI Authorization Tool")
    print("=" * 35)
    
    # Проверяем зависимости
    check_dependencies()
    
    # Импортируем PyQt6 только после проверки зависимостей
    from PyQt6.QtCore import QUrl
    from PyQt6.QtWidgets import QApplication, QMainWindow
    from PyQt6.QtWebEngineCore import QWebEngineUrlSchemeHandler, QWebEngineUrlScheme
    from PyQt6.QtWebEngineWidgets import QWebEngineView
    
    # Устанавливаем фильтрованный stderr
    original_stderr = sys.stderr
    sys.stderr = FilteredStderr(original_stderr)
    
    try:
        # Регистрируем кастомную схему до создания приложения
        scheme = QWebEngineUrlScheme(b"hhandroid")
        scheme.setFlags(QWebEngineUrlScheme.Flag.SecureScheme)
        QWebEngineUrlScheme.registerScheme(scheme)
        
        oauth_client = SimpleOAuthClient()
        
        app = QApplication(sys.argv)
        
        window = WebViewWindow(oauth_client)
        window.main_window.show()
        
        app.exec()
    finally:
        # Восстанавливаем stderr
        sys.stderr = original_stderr


if __name__ == "__main__":
    main()