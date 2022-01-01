from rest_framework import response, status
from todoapp.serializers import TodosListSerializer, TodosSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todoapp.models import TodosList, Todos
from rest_framework.permissions import IsAuthenticated

class TodosListApiView(ListCreateAPIView):
    """GET POST- List and Create TodosList data."""
    serializer_class = TodosListSerializer
    permission_classes = (IsAuthenticated, )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return TodosList.objects.filter(owner=self.request.user)

class TodosListDetailApiView(RetrieveUpdateDestroyAPIView):
    """PUT DELETE RETRIEVE- Get, Update and Delete particular TodosList data."""
    serializer_class = TodosListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TodosList.objects.filter(owner=self.request.user)

class TodosApiView(ListCreateAPIView):
    """GET POST- List and Create Todos data."""
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            todo_list_num = request.data.get('todo_list')
            # Check if the todo_list belongs to the user itself
            todo_list = TodosList.objects.filter(pk=todo_list_num,owner=self.request.user)
            if todo_list.exists():
                serializer.save()
                return response.Response({'success':"Todo created."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({'error':"No such todo_list exists"}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'error':"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        todolist = TodosList.objects.filter(owner=self.request.user)
        if todolist.exists():
            return Todos.objects.filter(todo_list=todolist[0])

class TodosDetailApiView(RetrieveUpdateDestroyAPIView):
    """PUT DELETE RETRIEVE- Get, Update and Delete particular Todos data.."""
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        todolist = TodosList.objects.filter(owner=self.request.user)
        if todolist.exists():
            return Todos.objects.filter(todo_list=todolist[0])