.PHONY: migrate makemigrations runserver test shell shell-plus lint format lint-fix

migrate:
	uv run python manage.py migrate

makemigrations:
	uv run python manage.py makemigrations

runserver:
	uv run python manage.py runserver

test:
	uv run pytest

shell:
	uv run python manage.py shell

shell-plus:
	uv run python manage.py shell_plus

lint:
	uv run ruff check .

format:
	uv run ruff format .

lint-fix:
	uv run ruff check --fix .
