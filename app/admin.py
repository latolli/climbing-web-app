from django.contrib import admin
from .models import Goal, Training, Grade

# Register your models here.
admin.site.register(Training)
admin.site.register(Grade)
admin.site.register(Goal)