from typing import Tuple
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodosList(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_owner = models.ManyToManyField(User, blank=True, related_name='shared')

class Todos(models.Model):
    name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodosList, on_delete=models.CASCADE)