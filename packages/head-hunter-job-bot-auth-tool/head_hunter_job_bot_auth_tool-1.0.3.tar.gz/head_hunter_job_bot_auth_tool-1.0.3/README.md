# HeadHunter Job Bot Auth Tool

[![PyPI version](https://badge.fury.io/py/head-hunter-job-bot-auth-tool.svg)](https://badge.fury.io/py/head-hunter-job-bot-auth-tool)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)(https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

GUI инструмент для авторизации в HeadHunter API через OAuth с графическим интерфейсом.

## 🚀 Возможности

- **Простая авторизация**: Графический интерфейс для OAuth авторизации в API hh.ru
- **Кроссплатформенность**: Работает на Windows, macOS и Linux
- **Автоматическое получение токена**: Выводит готовый к использованию токен в формате JSON
- **Безопасность**: Использует официальные OAuth параметры HeadHunter API
- **Простая установка**: Устанавливается через `pipx` одной командой

## 📦 Установка

### Установка через pipx (рекомендуется)

#### Установка pipx (если не установлен)

**На Windows:**

Сначала установите Scoop:
```powershell
# Разрешить выполнение скриптов
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Установить Scoop
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

После установки Scoop откройте консоль заново и установите pipx:
```cmd
scoop install pipx
pipx ensurepath

# Перезапустите командную строку после установки
```

**На Linux/macOS:**
```bash
# Ubuntu/Debian
sudo apt install pipx

# macOS (через Homebrew)
brew install pipx
pipx ensurepath
```

#### Установка пакета

**На Linux/macOS:**
```bash
pipx install head-hunter-job-bot-auth-tool
```

**На Windows:**
```cmd
pipx install head-hunter-job-bot-auth-tool
```

## 🔧 Требования

- **Python**: 3.9 или выше
- **PyQt6**: Для графического интерфейса
- **PyQt6-WebEngine**: Для веб-компонентов
- **requests**: Для HTTP запросов

Все зависимости устанавливаются автоматически.

## 🏃‍♂️ Использование

### Базовое использование

**Важно**: После установки утилиты перед первым запуском необходимо открыть консоль заново.

После установки запустите инструмент командой:

**На Linux/macOS:**
```bash
head-hunter-job-bot-auth-tool
```

**На Windows:**
```cmd
head-hunter-job-bot-auth-tool
```

### Опции командной строки

**На Linux/macOS:**
```bash
# Показать справку
head-hunter-job-bot-auth-tool --help

# Показать версию
head-hunter-job-bot-auth-tool --version
```

**На Windows:**
```cmd
# Показать справку
head-hunter-job-bot-auth-tool --help

# Показать версию
head-hunter-job-bot-auth-tool --version
```

### Процесс авторизации

1. **Запуск**: Выполните команду `head-hunter-job-bot-auth-tool`
2. **Авторизация**: Откроется окно браузера с формой входа на hh.ru
3. **Вход**: Введите ваши учетные данные HeadHunter
4. **Разрешение**: Подтвердите доступ к API
5. **Получение токена**: Токен будет выведен в консоль в формате JSON

### Пример результата

```json
{
  "access_token": "v3.r.123456789.abc...",
  "refresh_token": "v3.r.987654321.def...",
  "access_expires_at": 1705234567
}
```

## 🔐 Безопасность

- Инструмент использует официальные OAuth параметры HeadHunter API
- Токены не сохраняются автоматически - вы контролируете их хранение
- Поддерживается стандартный OAuth 2.0 flow
- Все соединения осуществляются через HTTPS

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.