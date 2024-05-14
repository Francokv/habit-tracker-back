from django.db import models

class Habit(models.Model):

    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Objetive(models.Model):

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    data_type = models.CharField(max_length=100)