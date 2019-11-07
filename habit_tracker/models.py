from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_registered = models.BooleanField(default=False)

    
class Habit(models.Model):
    user = models.ForeignKey(to='User', related_name="habits", on_delete=models.CASCADE, blank=True, null=True)
    goal = models.TextField()
    title = models.CharField(max_length=255, blank=False, null=False)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Log(models.Model):
    habit = models.ForeignKey(to='Habit', related_name='logs', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    amount = models.PositiveIntegerField(blank=False, null=True)
    achievement = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.description
