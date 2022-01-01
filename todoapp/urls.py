from django.urls import path
from todoapp.views import (
    TodosListApiView, 
    TodosListDetailApiView,
    TodosApiView,
    TodosDetailApiView,
    TodosListBriefView
)

urlpatterns = [
    path('todoslist/', TodosListApiView.as_view()),
    path('todoslist/<int:pk>', TodosListDetailApiView.as_view()),
    path('todoslistall/<int:pk>', TodosListBriefView.as_view()),
    path('todos/', TodosApiView.as_view()),
    path('todos/<int:pk>', TodosDetailApiView.as_view()),
]