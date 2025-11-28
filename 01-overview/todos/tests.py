from django.test import TestCase
from django.urls import reverse
from datetime import date, timedelta
from .models import Todo


class TodoModelTest(TestCase):
    """Test the Todo model"""

    def test_todo_creation(self):
        """Test creating a TODO item"""
        todo = Todo.objects.create(
            title="Test TODO",
            description="Test description"
        )
        self.assertEqual(todo.title, "Test TODO")
        self.assertEqual(todo.description, "Test description")
        self.assertFalse(todo.completed)
        self.assertIsNotNone(todo.created_at)
        self.assertIsNotNone(todo.updated_at)

    def test_todo_str_representation(self):
        """Test the string representation of TODO"""
        todo = Todo.objects.create(title="My Test TODO")
        self.assertEqual(str(todo), "My Test TODO")

    def test_todo_completion_toggle(self):
        """Test toggling TODO completion status"""
        todo = Todo.objects.create(title="Toggle Test")
        self.assertFalse(todo.completed)

        todo.completed = True
        todo.save()
        self.assertTrue(todo.completed)

        todo.completed = False
        todo.save()
        self.assertFalse(todo.completed)

    def test_todo_default_completed_is_false(self):
        """Test that new TODOs are not completed by default"""
        todo = Todo.objects.create(title="New TODO")
        self.assertFalse(todo.completed)

    def test_todo_optional_description(self):
        """Test creating TODO without description"""
        todo = Todo.objects.create(title="No Description")
        self.assertEqual(todo.description, None)

    def test_todo_with_due_date(self):
        """Test creating TODO with due date"""
        due_date = date.today() + timedelta(days=7)
        todo = Todo.objects.create(
            title="Due Date Test",
            due_date=due_date
        )
        self.assertEqual(todo.due_date, due_date)

    def test_todo_optional_due_date(self):
        """Test creating TODO without due date"""
        todo = Todo.objects.create(title="No Due Date")
        self.assertIsNone(todo.due_date)


class TodoListViewTest(TestCase):
    """Test the TODO list view"""

    def setUp(self):
        """Create test TODOs"""
        self.url = reverse('todo_list')
        Todo.objects.create(title="Test TODO 1", description="Description 1")
        Todo.objects.create(title="Test TODO 2", completed=True)

    def test_list_view_status_code(self):
        """Test that list view returns 200"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_list_view_uses_correct_template(self):
        """Test that list view uses the correct template"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'todos/todo_list.html')

    def test_list_view_contains_todos(self):
        """Test that list view displays TODOs"""
        response = self.client.get(self.url)
        self.assertContains(response, "Test TODO 1")
        self.assertContains(response, "Test TODO 2")

    def test_list_view_empty_state(self):
        """Test list view when no TODOs exist"""
        Todo.objects.all().delete()
        response = self.client.get(self.url)
        self.assertContains(response, "No TODOs yet")


class TodoCreateViewTest(TestCase):
    """Test the TODO create view"""

    def setUp(self):
        self.url = reverse('todo_create')

    def test_create_view_status_code(self):
        """Test that create view returns 200"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create_view_uses_correct_template(self):
        """Test that create view uses the correct template"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'todos/todo_form.html')

    def test_create_todo_post(self):
        """Test creating a TODO via POST"""
        data = {
            'title': 'New TODO',
            'description': 'New Description'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Todo.objects.count(), 1)

        todo = Todo.objects.first()
        self.assertEqual(todo.title, 'New TODO')
        self.assertEqual(todo.description, 'New Description')
        self.assertFalse(todo.completed)

    def test_create_todo_without_description(self):
        """Test creating TODO without description"""
        data = {'title': 'Only Title'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 1)

    def test_create_todo_with_due_date(self):
        """Test creating TODO with due date"""
        due_date = date.today() + timedelta(days=7)
        data = {
            'title': 'TODO with Due Date',
            'due_date': due_date.strftime('%Y-%m-%d')
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        todo = Todo.objects.first()
        self.assertEqual(todo.due_date, due_date)


class TodoUpdateViewTest(TestCase):
    """Test the TODO update/edit view"""

    def setUp(self):
        self.todo = Todo.objects.create(
            title="Original Title",
            description="Original Description"
        )
        self.url = reverse('todo_edit', args=[self.todo.pk])

    def test_update_view_status_code(self):
        """Test that update view returns 200"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_update_view_uses_correct_template(self):
        """Test that update view uses the correct template"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'todos/todo_form.html')

    def test_update_todo_post(self):
        """Test updating a TODO via POST"""
        data = {
            'title': 'Updated Title',
            'description': 'Updated Description'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after success

        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated Title')
        self.assertEqual(self.todo.description, 'Updated Description')

    def test_update_todo_with_due_date(self):
        """Test updating TODO to add due date"""
        due_date = date.today() + timedelta(days=5)
        data = {
            'title': 'Updated with Due Date',
            'description': 'Description',
            'due_date': due_date.strftime('%Y-%m-%d')
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)

        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, 'Updated with Due Date')
        self.assertEqual(self.todo.due_date, due_date)

    def test_update_view_404_for_invalid_todo(self):
        """Test that updating invalid TODO ID returns 404"""
        url = reverse('todo_edit', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TodoDetailViewTest(TestCase):
    """Test the TODO detail view"""

    def setUp(self):
        self.todo = Todo.objects.create(
            title="Detail Test",
            description="Detail Description"
        )
        self.url = reverse('todo_detail', args=[self.todo.pk])

    def test_detail_view_status_code(self):
        """Test that detail view returns 200"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_detail_view_uses_correct_template(self):
        """Test that detail view uses the correct template"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'todos/todo_detail.html')

    def test_detail_view_contains_todo_info(self):
        """Test that detail view displays TODO information"""
        response = self.client.get(self.url)
        self.assertContains(response, "Detail Test")
        self.assertContains(response, "Detail Description")

    def test_detail_view_404_for_invalid_todo(self):
        """Test that invalid TODO ID returns 404"""
        url = reverse('todo_detail', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TodoToggleViewTest(TestCase):
    """Test the TODO toggle view"""

    def setUp(self):
        self.todo = Todo.objects.create(title="Toggle Test")
        self.url = reverse('todo_toggle', args=[self.todo.pk])

    def test_toggle_todo_to_completed(self):
        """Test toggling TODO to completed"""
        self.assertFalse(self.todo.completed)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)  # Redirect
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.completed)

    def test_toggle_todo_to_incomplete(self):
        """Test toggling TODO back to incomplete"""
        self.todo.completed = True
        self.todo.save()

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

        self.todo.refresh_from_db()
        self.assertFalse(self.todo.completed)


class TodoDeleteViewTest(TestCase):
    """Test the TODO delete view"""

    def setUp(self):
        self.todo = Todo.objects.create(title="Delete Test")
        self.url = reverse('todo_delete', args=[self.todo.pk])

    def test_delete_view_get_status_code(self):
        """Test that delete confirmation page returns 200"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_delete_view_uses_correct_template(self):
        """Test that delete view uses the correct template"""
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'todos/todo_confirm_delete.html')

    def test_delete_todo_post(self):
        """Test deleting a TODO via POST"""
        self.assertEqual(Todo.objects.count(), 1)
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)  # Redirect after delete
        self.assertEqual(Todo.objects.count(), 0)

    def test_delete_view_404_for_invalid_todo(self):
        """Test that deleting invalid TODO ID returns 404"""
        url = reverse('todo_delete', args=[9999])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)
