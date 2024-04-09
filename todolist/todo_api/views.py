from rest_framework import viewsets
from .models import ToDoList
from .serializer import TodoSerializer
from django.core.cache import cache
from rest_framework.response import Response


class TodoListApiView(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = TodoSerializer

    # метод должен называться также, как в ModelViewSet
    # метод, который мы хотим кешировать
    
    def list(self, request, *args, **kwargs):
        cached_data = cache.get('todo_list')
        if cached_data:
            return Response(cached_data)

        queryset = self.filter_queryset(self.queryset)
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        
        cache.set('todo_list', data, timeout=120)
        return Response(data)
        
            
    

