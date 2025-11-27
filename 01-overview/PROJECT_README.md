# Django TODO App

A simple yet functional TODO application built with Django for the AI Dev Tools Zoomcamp 2025 - Module 1 homework.

## Overview

This project demonstrates the use of AI development tools (Claude Code, GitHub Copilot, etc.) to build a complete Django web application. The app allows users to create, view, update, and delete TODO items with a clean, modern interface.

## Features

- ✅ Create new TODO items with title and description
- ✅ View all TODOs in a list
- ✅ Mark TODOs as complete/incomplete
- ✅ View detailed information for each TODO
- ✅ Delete TODO items
- ✅ Admin interface for managing TODOs
- ✅ Responsive, modern UI with visual status indicators
- ✅ Comprehensive test suite (23 tests)

## Tech Stack

- **Python**: 3.10+
- **Django**: 5.2.8
- **uv**: Modern Python package manager
- **pytest**: Testing framework
- **pytest-django**: Django integration for pytest
- **SQLite**: Database (default Django DB)

## Project Structure

```
01-overview/
├── .venv/                  # Virtual environment
├── todo_project/           # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── todos/                  # Main TODO app
│   ├── models.py          # Todo model
│   ├── views.py           # View logic
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   ├── tests.py           # Test suite
│   ├── templates/todos/   # HTML templates
│   │   ├── base.html
│   │   ├── todo_list.html
│   │   ├── todo_form.html
│   │   ├── todo_detail.html
│   │   └── todo_confirm_delete.html
│   └── migrations/        # Database migrations
├── manage.py              # Django management script
├── Makefile               # Common commands
├── pyproject.toml         # Project dependencies
├── uv.lock                # Dependency lock file
├── pytest.ini             # Pytest configuration
└── db.sqlite3             # SQLite database

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- uv package manager

### Installation

1. **Install uv** (if not already installed):
   ```bash
   brew install uv
   ```

2. **Navigate to the project directory**:
   ```bash
   cd 01-overview
   ```

3. **Create and activate virtual environment**:
   ```bash
   uv venv
   source .venv/bin/activate  # On macOS/Linux
   ```

4. **Install dependencies**:
   ```bash
   uv sync
   ```

5. **Run migrations**:
   ```bash
   uv run python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access):
   ```bash
   uv run python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   uv run python manage.py runserver
   ```

8. **Access the application**:
   - Main app: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## Using the Makefile

The project includes a Makefile for common commands:

```bash
make migrate          # Run database migrations
make makemigrations   # Create new migrations
make runserver        # Start development server
make test             # Run tests with pytest
make shell            # Open Django shell
make superuser        # Create superuser
```

## Running Tests

The project includes a comprehensive test suite with 23 tests covering:
- Model creation and behavior
- All CRUD operations
- URL routing and views
- Template rendering
- Error handling

### Run with pytest:
```bash
make test
# or
uv run pytest
```

### Run with Django test runner:
```bash
uv run python manage.py test
```

### Test Coverage:
- ✅ 5 model tests
- ✅ 4 list view tests
- ✅ 4 create view tests
- ✅ 4 detail view tests
- ✅ 2 toggle view tests
- ✅ 4 delete view tests

All tests passing: **23/23** ✓

## Usage

### Creating a TODO

1. Click "Add New TODO" or navigate to `/create/`
2. Enter a title (required) and description (optional)
3. Click "Create TODO"

### Viewing TODOs

- Home page (`/`) displays all TODOs
- Click on a TODO title to view details
- Completed TODOs have a green background
- Pending TODOs have a white background

### Completing/Uncompleting a TODO

- Click the "Complete" or "Undo" button on any TODO
- Status updates immediately

### Deleting a TODO

1. Click "Delete" on a TODO
2. Confirm deletion on the confirmation page

## Database Schema

### Todo Model

| Field | Type | Description |
|-------|------|-------------|
| id | AutoField | Primary key |
| title | CharField(200) | TODO title (required) |
| description | TextField | TODO description (optional) |
| completed | BooleanField | Completion status (default: False) |
| created_at | DateTimeField | Creation timestamp (auto) |
| updated_at | DateTimeField | Last update timestamp (auto) |

## Development Notes

- Built using Django class-based views (ListView, CreateView, DetailView, DeleteView)
- Function-based view for toggle functionality
- Templates use Django template inheritance
- Inline CSS for simplicity and portability
- All forms include CSRF protection
- Database uses Django ORM with migrations

## Homework Questions Answered

This project addresses all Module 1 homework questions:

1. ✅ **Question 1**: Django installed via uv
2. ✅ **Question 2**: Project created with settings.py, manage.py, urls.py, wsgi.py
3. ✅ **Question 3**: Models created, migrations run, admin panel configured, Makefile created
4. ✅ **Question 4**: Views, URLs, admin, and tests implemented
5. ✅ **Question 5**: Templates configured with proper inheritance
6. ✅ **Question 6**: Tests run successfully with both pytest and Django test runner

## Future Enhancements

Potential improvements for this project:

- [ ] Edit TODO functionality
- [ ] Due dates and reminders
- [ ] Priority levels (high, medium, low)
- [ ] Categories/tags for TODOs
- [ ] Search and filter functionality
- [ ] User authentication and per-user TODOs
- [ ] REST API endpoints
- [ ] Frontend framework integration (React, Vue)

## License

This project is created for educational purposes as part of the DataTalks.Club AI Dev Tools Zoomcamp 2025.

## Acknowledgments

- Built with assistance from AI dev tools (Claude Code)
- Part of [DataTalks.Club AI Dev Tools Zoomcamp 2025](https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/)
