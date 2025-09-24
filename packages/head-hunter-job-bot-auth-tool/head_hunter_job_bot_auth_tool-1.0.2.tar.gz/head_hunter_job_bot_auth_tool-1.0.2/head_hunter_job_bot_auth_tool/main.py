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
from urllib.parse import parse_qs, urlencode, urlsplit
from typing import Dict, Any

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


def create_url_scheme_handler(parent_window):
    """Создает обработчик URL схемы"""
    from PyQt6.QtWebEngineCore import QWebEngineUrlSchemeHandler
    
    class HHAndroidUrlSchemeHandler(QWebEngineUrlSchemeHandler):
        def __init__(self, parent_window):
            super().__init__()
            self.parent_window = parent_window

        def requestStarted(self, info):
            url = info.requestUrl().toString()
            if url.startswith("hhandroid://"):
                self.parent_window.handle_redirect_uri(url)
    
    return HHAndroidUrlSchemeHandler(parent_window)


def create_web_view_window(oauth_client):
    """Создает окно с веб-браузером для авторизации"""
    from PyQt6.QtCore import QUrl
    from PyQt6.QtWidgets import QMainWindow
    from PyQt6.QtWebEngineWidgets import QWebEngineView
    
    class WebViewWindow(QMainWindow):
        def __init__(self, oauth_client):
            super().__init__()
            self.oauth_client = oauth_client
            self.setup_ui()
            
        def setup_ui(self):
            # Настройка WebEngineView
            self.web_view = QWebEngineView()
            self.setCentralWidget(self.web_view)
            self.setWindowTitle("Авторизация на HH.RU")
            
            # Обработчик кастомной схемы
            self.hhandroid_handler = create_url_scheme_handler(self)
            profile = self.web_view.page().profile()
            profile.installUrlSchemeHandler(b"hhandroid", self.hhandroid_handler)
            
            # Настройки окна для мобильного вида
            self.resize(480, 800)
            self.web_view.setUrl(QUrl(self.oauth_client.authorize_url))

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
                    self.close()
                except Exception as e:
                    print(f"❗ Ошибка при получении токена: {e}")
            else:
                print("❗ Не удалось получить код авторизации")
    
    return WebViewWindow(oauth_client)


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
        
        window = create_web_view_window(oauth_client)
        window.show()
        
        app.exec()
    finally:
        # Восстанавливаем stderr
        sys.stderr = original_stderr


if __name__ == "__main__":
    main()