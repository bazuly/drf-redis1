from rest_framework import serializers
from .models import ToDoList


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'