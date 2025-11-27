# Homework 1: Introduction to AI Dev Tools Zoomcamp 2025

**Course**: AI Dev Tools Zoomcamp 2025
**Module**: 1 - Introduction to Vibe Coding
**Due Date**: November 27, 2025 18:00 (local time)

---

## Question 1. Install Django (1 point)

**Answer**: ✅ **Completed**

Django 5.2.8 has been installed using `uv` package manager.

**Installation command**:
```bash
uv add django
```

**Verification**:
```bash
uv run django-admin --version
# Output: 5.2.8
```

**Files created**:
- `pyproject.toml` - Contains Django dependency
- `uv.lock` - Lock file with exact versions

---

## Question 2. Project and App (1 point)

**Answer**: ✅ **Completed**

Django project `todo_project` and app `todos` have been created.

**Commands used**:
```bash
uv run django-admin startproject todo_project .
uv run python manage.py startapp todos
```

**Required files verified**:
- ✅ `todo_project/settings.py` - Project settings
- ✅ `manage.py` - Django management script
- ✅ `todo_project/urls.py` - URL configuration
- ✅ `todo_project/wsgi.py` - WSGI configuration
- ✅ `todo_project/asgi.py` - ASGI configuration (bonus)

**Project structure**:
```
01-overview/
├── manage.py
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── todos/
    ├── models.py
    ├── views.py
    ├── admin.py
    ├── tests.py
    └── ...
```

---

## Question 3. Django Models (1 point)

**Answer**: ✅ **Completed**

### Todo Model Created

**File**: `todos/models.py`

```python
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
```

### Tasks Completed:

✅ **Run the application**
```bash
uv run python manage.py runserver
# Application running at http://localhost:8000/
```

✅ **Add models to admin panel**
**File**: `todos/admin.py`
```python
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created_at', 'updated_at']
    list_filter = ['completed', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['completed']
```

✅ **Run migrations**
```bash
uv run python manage.py makemigrations
# Created: todos/migrations/0001_initial.py

uv run python manage.py migrate
# Applied all migrations successfully
```

✅ **Create Makefile**
**File**: `Makefile`
```makefile
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
```

---

## Question 4. TODO Logic (1 point)

**Answer**: ✅ **Completed**

### Files Implemented:

✅ **views.py** - `todos/views.py`
- `TodoListView` - List all TODOs
- `TodoCreateView` - Create new TODO
- `TodoDetailView` - View TODO details
- `TodoDeleteView` - Delete TODO
- `toggle_todo` - Toggle completion status

✅ **urls.py** - `todos/urls.py`
```python
urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/toggle/', views.toggle_todo, name='todo_toggle'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='todo_delete'),
]
```

✅ **admin.py** - Configured in Question 3 (see above)

✅ **tests.py** - `todos/tests.py`
- 23 comprehensive tests covering all functionality
- Model tests (5 tests)
- View tests (18 tests)
- All tests passing

---

## Question 5. Templates (1 point)

**Answer**: ✅ **Completed**

### Template Configuration:

✅ **INSTALLED_APPS in settings.py**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todos',  # ← Added
]
```

✅ **TEMPLATES['DIRS'] in settings.py**
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Empty, using app-level templates
        'APP_DIRS': True,
        ...
    }
]
```

✅ **TEMPLATES['APP_DIRS'] in settings.py**
```python
'APP_DIRS': True  # ← Enabled for app-level templates
```

✅ **App's urls.py**
- Created `todos/urls.py` with all URL patterns
- Included in project's `urls.py`:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),
]
```

### Templates Created:

**Directory**: `todos/templates/todos/`

- ✅ `base.html` - Base template with navigation and styling
- ✅ `todo_list.html` - List all TODOs
- ✅ `todo_form.html` - Create TODO form
- ✅ `todo_detail.html` - TODO detail view
- ✅ `todo_confirm_delete.html` - Delete confirmation

All templates use template inheritance extending `base.html`.

---

## Question 6. Tests (1 point)

**Answer**: ✅ **Completed**

### Test Suite: 23 Tests

**File**: `todos/tests.py`

### Test Results:

✅ **pytest**
```bash
uv run pytest
# ====== 23 passed in 0.13s ======
```

✅ **python manage.py test**
```bash
uv run python manage.py test
# Ran 23 tests in 0.029s
# OK
```

### Test Coverage:

**Model Tests (5 tests)**:
- ✅ test_todo_creation
- ✅ test_todo_str_representation
- ✅ test_todo_completion_toggle
- ✅ test_todo_default_completed_is_false
- ✅ test_todo_optional_description

**View Tests (18 tests)**:
- List View: 4 tests
- Create View: 4 tests
- Detail View: 4 tests
- Toggle View: 2 tests
- Delete View: 4 tests

**All tests passing**: ✅ 23/23

---

## Additional Information

### Tools Used:
- **AI Assistant**: Claude Code (Anthropic)
- **Package Manager**: uv (Astral)
- **Python**: 3.10.10
- **Django**: 5.2.8
- **Testing**: pytest 9.0.1, pytest-django 4.11.1

### Project Features:
- ✅ Full CRUD operations for TODOs
- ✅ Admin panel integration
- ✅ Responsive UI with inline CSS
- ✅ Comprehensive test coverage
- ✅ Clean, modern interface
- ✅ Makefile for common commands

### Documentation:
- ✅ `PROJECT_README.md` - Complete setup and usage guide
- ✅ `spec.md` - Project specification with checklist
- ✅ `Makefile` - Common development commands
- ✅ This homework submission

---

## Status

**Status**: ✅ **Completed**
**All Questions**: 6/6 answered
**All Tests**: 23/23 passing
**Submission Date**: November 27, 2025