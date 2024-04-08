from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    status = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    
    def __str__(self) -> str:
        return self.title
    