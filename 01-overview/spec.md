# Django TODO App - Project Specification

## Project Overview

Build a Django TODO application to demonstrate AI dev tools usage for the AI Dev Tools Zoomcamp Module 1 homework.

## Requirements

- Python 3.12+
- uv (modern Python package manager)
- Django (latest stable version)
- pytest (for testing)
- pytest-django (for Django test integration)

---

## Implementation Checklist

### Phase 1: Environment Setup

- [x] Install uv (if not already installed): `brew install uv`
- [x] Initialize uv project: `uv init` (or use existing setup)
- [x] Create/sync virtual environment with uv: `uv venv`
- [x] Install Django: `uv add django`
- [x] Install testing dependencies: `uv add --dev pytest pytest-django`
- [x] Create `pytest.ini` or configure pytest in `pyproject.toml`
- [x] Verify Django installation: `uv run django-admin --version`

### Phase 2: Project Structure

- [x] Create Django project: `uv run django-admin startproject todo_project .`
- [x] Create Django app: `uv run python manage.py startapp todos`
- [x] Verify project structure includes:
  - [x] `settings.py`
  - [x] `manage.py`
  - [x] `urls.py`
  - [x] `wsgi.py`

### Phase 3: Models & Database

- [x] Define TODO model in `todos/models.py` with fields:
  - [x] Title (CharField)
  - [x] Description (TextField, optional)
  - [x] Completed (BooleanField)
  - [x] Created date (DateTimeField, auto)
  - [x] Updated date (DateTimeField, auto)
- [x] Add `__str__` method to model
- [X] Register app in `INSTALLED_APPS` (settings.py)
- [X] Create initial migrations (`makemigrations`)
- [X] Run migrations (`migrate`)
- [X] Register models in `admin.py`
- [X] Create superuser for admin access
- [x] Create Makefile with common commands (using uv):
  - [x] `migrate` - run migrations: `uv run python manage.py migrate`
  - [x] `makemigrations` - create migrations: `uv run python manage.py makemigrations`
  - [x] `runserver` - start dev server: `uv run python manage.py runserver`
  - [x] `test` - run tests: `uv run pytest`
  - [x] `shell` - open Django shell: `uv run python manage.py shell`
  
### Phase 4: Views & URL Routing

- [x] Create views in `todos/views.py`:
  - [x] List all TODOs (index/list view)
  - [x] Create new TODO (create view)
  - [x] Mark TODO as complete/incomplete (toggle view)
  - [x] Delete TODO (delete view)
  - [x] Detail view for single TODO (optional)
- [x] Configure URL patterns in `todos/urls.py`
- [x] Include app URLs in project's `urls.py`
- [x] Add admin URLs to project's `urls.py`

### Phase 5: Templates

- [x] Configure template settings in `settings.py`:
  - [x] Set `TEMPLATES['DIRS']` for project-level templates
  - [x] Verify `TEMPLATES['APP_DIRS']` is True
- [x] Create `templates/` directory structure:
  - [x] `todos/base.html` - base template
  - [x] `todos/todo_list.html` - list all TODOs
  - [x] `todos/todo_form.html` - create/edit form
  - [x] `todos/todo_detail.html` - single TODO view (optional)
- [ ] Add basic CSS styling (optional but recommended)
- [ ] Implement template inheritance

### Phase 6: Testing

- [X] Write tests in `todos/tests.py`:
  - [X] Test TODO model creation
  - [X] Test TODO model string representation
  - [X] Test TODO completion toggle
  - [X] Test list view
  - [X] Test create view
  - [X] Test delete view
- [X] Run tests using:
  - [X] `pytest`
  - [X] `python manage.py test`
- [X] Ensure all tests pass

### Phase 7: Documentation & Cleanup

- [ ] Update `.gitignore` for Django-specific files:
  - [ ] `.venv/` (virtual environment)
  - [ ] `*.pyc`
  - [ ] `__pycache__/`
  - [ ] `db.sqlite3`
  - [ ] `.env`
  - [ ] Static files
  - [ ] **Note**: Keep `uv.lock` in git for reproducible builds
- [ ] Create/update `README.md` with:
  - [ ] Project description
  - [ ] Setup instructions
  - [ ] How to run the application
  - [ ] How to run tests
  - [ ] Makefile commands
- [ ] Verify all homework questions are answered in `homework.md`

### Phase 8: Optional Enhancements

- [ ] Add TODO editing functionality
- [ ] Add due dates to TODOs
- [ ] Add priority levels
- [ ] Add filtering (completed/incomplete)
- [ ] Add search functionality
- [ ] Add pagination for TODO list
- [ ] Add static files configuration
- [ ] Deploy to a hosting platform

---

## Project Structure

```
01-overview/
├── .venv/                  # Virtual environment (gitignored)
├── todo_project/           # Django project
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Project URL config
│   ├── wsgi.py             # WSGI config
│   └── asgi.py             # ASGI config
├── todos/                  # Django app
│   ├── migrations/         # Database migrations
│   ├── templates/todos/    # App templates
│   ├── __init__.py
│   ├── admin.py            # Admin registration
│   ├── apps.py             # App config
│   ├── models.py           # TODO model
│   ├── tests.py            # Test cases
│   ├── urls.py             # App URL config
│   └── views.py            # View functions/classes
├── manage.py               # Django management script
├── Makefile                # Common commands
├── pyproject.toml          # Project metadata & dependencies (uv)
├── uv.lock                 # Lock file for dependencies (commit to git)
├── .python-version         # Python version for uv (optional)
├── pytest.ini              # Pytest configuration
├── db.sqlite3              # SQLite database (gitignored)
├── README.md               # Project documentation
├── homework.md             # Homework submission
└── spec.md                 # This file
```

---

## Homework Questions Reference

1. **Question 1**: Install Django
2. **Question 2**: Create project with settings.py, manage.py, urls.py, wsgi.py
3. **Question 3**: Create models, run app, add to admin, run migrations, create Makefile
4. **Question 4**: Implement TODO logic in views.py, urls.py, admin.py, tests.py
5. **Question 5**: Configure templates (INSTALLED_APPS, TEMPLATES['DIRS'], TEMPLATES['APP_DIRS'])
6. **Question 6**: Write and run tests (pytest, python manage.py test)

---

## Notes

- **Using uv**: This project uses [uv](https://github.com/astral-sh/uv) for fast, modern Python package management
  - All Django commands should be prefixed with `uv run` (e.g., `uv run python manage.py runserver`)
  - Dependencies are managed in `pyproject.toml` instead of `requirements.txt`
  - Use `uv add <package>` to add dependencies, `uv add --dev <package>` for dev dependencies
- Use AI dev tools (Claude Code, GitHub Copilot, Cursor, etc.) to assist with implementation
- Follow Django best practices and conventions
- Keep code clean and well-documented
- Test thoroughly before submission
- Due date: November 27, 2025 18:00 (local time)
