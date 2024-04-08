from django.urls import path, include
from todo_api.views import TodoListApiView
from rest_framework import routers
from django.contrib import admin


router = routers.DefaultRouter()
router.register(r'api/todo_api', TodoListApiView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
