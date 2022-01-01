from django.urls import path
from todoapp.views import (
    TodosListApiView, 
    TodosListDetailApiView,
)
urlpatterns = [
    path('todoslist', TodosListApiView.as_view()),
    path('todoslist/<int:pk>', TodosListDetailApiView.as_view()),
]