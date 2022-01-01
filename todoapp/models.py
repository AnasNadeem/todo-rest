from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodosList(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Todos(models.Model):
    name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodosList, on_delete=models.CASCADE)