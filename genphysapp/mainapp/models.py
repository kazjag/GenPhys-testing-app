"""
Creating models
"""
from django.db import models

# Create your models here.
class Feedback(models.Model):
    """
    class for feedback
    """
    text = models.TextField() #текст отзыва
    created_date = models.DateTimeField(auto_now_add=True) #дата написания
    author = models.CharField(max_length=50) #автор

class Problem(models.Model):
    """
    class for optics problem
    """
    task_text = models.TextField()
    left_border = models.DecimalField(decimal_places=5, max_digits=10)
    right_border = models.DecimalField(decimal_places=5, max_digits=10)
    answer = models.CharField(max_length=150)
    commentary = models.CharField(max_length=300, default = "")
