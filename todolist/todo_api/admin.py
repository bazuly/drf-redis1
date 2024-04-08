from django.contrib import admin
from .models import ToDoList


class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']
    search_fields = ['title']
    save_on_top = True

admin.site.register(ToDoList, ToDoListAdmin)