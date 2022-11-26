from todoapp.models import TodosList, Todos
from rest_framework.serializers import ModelSerializer


class TodosListSerializer(ModelSerializer):
    class Meta:
        model = TodosList
        fields = '__all__'


class TodosSerializer(ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['todo_list'] = TodosListSerializer(instance.todo_list).data
        return response
