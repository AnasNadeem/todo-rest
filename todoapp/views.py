from todoapp.serializers import TodosListSerializer, TodosSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todoapp.models import TodosList, Todos

class TodosListApiView(ListCreateAPIView):
    """GET POST- List and Create TodosList data."""
    serializer_class = TodosListSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return TodosList.objects.filter(owner=self.request.user)

class TodosListDetailApiView(RetrieveUpdateDestroyAPIView):
    """PUT DELETE RETRIEVE- Get, Update and Delete particular TodosList data."""
    serializer_class = TodosListSerializer

    def get_queryset(self):
        return TodosList.objects.filter(owner=self.request.user)