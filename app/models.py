from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Training(models.Model):
    trainingId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="training", null=True)
    date = models.DateField()

class Grade(models.Model):
    gradeId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="grade", null=True)
    date = models.DateField()
    grade = models.IntegerField()

class Goal(models.Model):
    goalId = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goal", null=True)
    title = models.CharField(max_length=300)
    done = models.BooleanField()
