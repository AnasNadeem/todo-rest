from django.urls import path
from todoapp.views import (
    TodosListApiView, 
    TodosListDetailApiView,
    TodosApiView,
    TodosDetailApiView
)

urlpatterns = [
    path('todoslist/', TodosListApiView.as_view()),
    path('todoslist/<int:pk>', TodosListDetailApiView.as_view()),
    path('todos/', TodosApiView.as_view()),
    path('todos/<int:pk>', TodosDetailApiView.as_view()),
]