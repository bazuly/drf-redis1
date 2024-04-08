from rest_framework import viewsets
from .models import ToDoList
from .serializer import TodoSerializer


class TodoListApiView(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = TodoSerializer
    
