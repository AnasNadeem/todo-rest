from django.contrib import admin
from todoapp.models import Todos, TodosList
# Register your models here.
admin.site.register(Todos)
admin.site.register(TodosList)