from rest_framework import serializers
from .models import Todo, User


# todo 하나를 조작하기 위한 serializer
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'completed', )

# todo_list를 만들기 위해서 user의 todo목록을 가져옴
class UserSerializer(serializers.ModelSerializer):
    todo_set = TodoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set', )