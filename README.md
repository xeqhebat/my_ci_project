# My CI Project

Проект для лабораторной работы по настройке CI с использованием GitHub Actions.

## Технологии

- Python 3.12
- Poetry (управление зависимостями и сборка)
- Ruff (линтер)
- Pytest + pytest-cov (тесты и покрытие)

## Установка и запуск

```bash
poetry install
poetry run pytest --cov=my_ci_project tests/
poetry run ruff check my_ci_project/
poetry build
