from rest_framework import response, status
from todoapp.serializers import TodosListSerializer, TodosSerializer
from todoapp.models import TodosList, Todos
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from django_filters import rest_framework as filters


class TodosListViewset(ModelViewSet):
    serializer_class = TodosListSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'owner',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return TodosList.objects.none()
        return TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id))


class TodosViewset(ModelViewSet):
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'is_completed', 'todo_list',)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            todo_list_num = request.data.get('todo_list')
            # Check if the todo_list belongs to the user itself
            todo_list = TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id),pk=todo_list_num)
            if todo_list.exists():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return response.Response({'error':"No such todo_list exists"}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'error':"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Todos.objects.none()
        todolists = TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id))
        all_todos = Todos.objects.none()
        for todolist in todolists:
            todos = todolist.todos_set.all()
            all_todos = all_todos | todos
        return all_todos
