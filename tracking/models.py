from django.db import models
from habit.models import Habit

class HabitTrackingData(models.Model):

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)
    
    extra_data = models.TextField(default='', blank=True)