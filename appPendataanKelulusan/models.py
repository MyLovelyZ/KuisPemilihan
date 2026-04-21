from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class 

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    is_banned = models.BooleanField(default=False)

class Question(models.Model):
    text = models.TextField()
    points = models.IntegerField(default=10)
    
class QuizResult(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_points = models.IntegerField()
    grade = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)