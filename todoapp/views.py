from rest_framework import response, status
from todoapp.serializers import TodosListSerializer, TodosSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todoapp.models import TodosList, Todos
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class TodosListApiView(ListCreateAPIView):
    """GET POST- List and Create TodosList data."""
    serializer_class = TodosListSerializer
    permission_classes = (IsAuthenticated, )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        try:
            return TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id))
        except:
            return None

class TodosListDetailApiView(RetrieveUpdateDestroyAPIView):
    """PUT DELETE RETRIEVE- Get, Update and Delete particular TodosList data."""
    serializer_class = TodosListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id))

class TodosListBriefView(GenericAPIView):
    """GET - List Of All Todos in TodoList."""
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticated, )
    def get(self, request, pk):
        check_todo_list = TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id), pk=pk)
        if check_todo_list.exists():
            all_todos = Todos.objects.filter(todo_list=check_todo_list[0])
            serializer = self.serializer_class(all_todos, many=True)
            return response.Response({'data':serializer.data}, status=status.HTTP_200_OK)
        return response.Response({'error':"No such Todoslist"}, status=status.HTTP_400_BAD_REQUEST)

class TodosApiView(ListCreateAPIView):
    """GET POST- List and Create Todos data."""
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            todo_list_num = request.data.get('todo_list')
            # Check if the todo_list belongs to the user itself
            todo_list = TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id),pk=todo_list_num)
            if todo_list.exists():
                serializer.save()
                return response.Response({'success':"Todo created."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({'error':"No such todo_list exists"}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({'error':"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        todolist = TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id))
        if todolist.exists():
            return Todos.objects.filter(todo_list__in=todolist)

class TodosDetailApiView(RetrieveUpdateDestroyAPIView):
    """PUT DELETE RETRIEVE- Get, Update and Delete particular Todos data.."""
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        todolist = TodosList.objects.filter(Q(owner=self.request.user) | Q(shared_owner__id=self.request.user.id))
        if todolist.exists():
            return Todos.objects.filter(todo_list=todolist[0])