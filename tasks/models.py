from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    completed = models.BooleanField(default=False)
    assigned_to = models.CharField(max_length=70, blank=False, default='')
    task_due_date = models.DateField()
   

