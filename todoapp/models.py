from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodosList(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_owner = models.ManyToManyField(User, blank=True, related_name='shared')

    def __str__(self):
        return f"{self.name}-{self.owner.username}"


class Todos(models.Model):
    name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodosList, on_delete=models.CASCADE)

    def __str__(self):
        return f"Task - {self.name} Status- {self.is_completed} Owner- {self.todo_list.owner.username} Main List-{self.todo_list.name} "