from django.test import Client, TestCase
from rest_framework import status
from django.core.cache import cache
from .models import ToDoList
from .serializer import TodoSerializer
import random
from rest_framework.test import APIClient


class TestCache(TestCase):
    """
    Проверка работы redis
    """

    def test_cache(self):
        todo_instance = ToDoList.objects.create(title='Test Cache',
                                                description='test cache description',
                                                status='done')
        serializer = TodoSerializer(todo_instance)
        todo_data = serializer.data
        
        client = Client()
        response = client.get('/api/todo_api/')
        assert response.status_code == status.HTTP_200_OK
        assert todo_data in response.data
        cached_data = response.data
        response_cached = client.get('/api/todo_api/')
        assert response_cached.status_code == status.HTTP_200_OK
        assert cached_data == response_cached.data
        cached_data_redis = cache.get('todo_list')
        assert cached_data_redis == cached_data
        


class LoadTest(TestCase):
    def setUp(self):
        for i in range(100):
            title = f'Task {i+1}'
            description = f'test cache description {i+1}'
            status = random.choice(['done', 'in progress'])
            ToDoList.objects.create(title=title,
                                    description=description,
                                    status=status)


    def test_get_objects(self):
        client = APIClient()
        response = client.get('/api/todo_api/')
        self.assertEqual(response.status_code, 200)
        todo_list = response.data
        # print(todo_list)
        self.assertEqual(len(todo_list['results']), 100)
        
        random_todo = random.choice(todo_list)
        response = client.get(f"/api/todo_api/{random_todo['id']}/")
        self.assertEqual(response.status_code, 200)