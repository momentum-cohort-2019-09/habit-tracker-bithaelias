from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    is_registered = models.BooleanField(default=False)
    
    
class Habit(models.Model):
    user = models.ForeignKey(to='User', related_name="habits", on_delete=models.CASCADE, blank=True, null=True)
    habit = models.CharField(max_length=255, blank=True, null=True)
    goal = models.PositiveIntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note

class Journal(models.Model):
    habit = models.ForeignKey(to='Habit', related_name='journal', on_delete=models.CASCADE, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    count = models.PositiveIntegerField(null=True, blank=True)
    met_goal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.note

   
