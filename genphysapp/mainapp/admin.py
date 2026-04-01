"""
Registering models
"""
#pylint: enable=no-member
from django.contrib import admin

# Register your models here.
from .models import Problem, Feedback

admin.site.register(Problem)
admin.site.register(Feedback)
#pylint: disable=no-member
