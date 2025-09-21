# Курсовая работа - Система управления привычками

## Описание проекта

RESTful API для управления привычками с напоминаниями в Telegram.

## Технологии

- Python 3.11+
- Django 4.2+
- Django REST Framework
- Celery + Redis
- PostgreSQL
- Telegram Bot API

## Установка

### 1. Клонирование репозитория
```bash
git clone <Egor-Farkov>
cd habit-tracker
```
# Запуск проекта с использованием Docker Compose

Этот файл `docker-compose.yml` определяет конфигурацию для запуска всех необходимых сервисов вашего проекта: веб-приложения Django, базы данных PostgreSQL, Redis и Celery (worker и beat).

## Предварительные требования

*   [Docker](https://docs.docker.com/get-docker/) установлен и работает.
*   [Docker Compose](https://docs.docker.com/compose/install/) установлен (обычно входит в состав Docker Desktop).
*   Файл `.env` с необходимыми переменными окружения (например, `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`).

## Процесс запуска

### 1. Сборка и запуск всех сервисов

Перейдите в корневую директорию вашего проекта (где находится файл `docker-compose.yml` и `Dockerfile`). Затем выполните следующую команду:

```bash
docker-compose up --build
```