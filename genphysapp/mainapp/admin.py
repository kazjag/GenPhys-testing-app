from django.contrib import admin

# Register your models here.
from .models import Problem, Feedback

admin.site.register(Problem)
admin.site.register(Feedback)