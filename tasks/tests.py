from django.test import TestCase
from django.urls import reverse
from tasks.models import Task
import pytest

# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"

@pytest.mark.django_db
def test_create_task2():
    task = Task.objects.create(
        title='Create this task'

    )
    assert task.title == "Create this task"