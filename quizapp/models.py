from django.db import models
from django.contrib.auth.models import User
class questionTable(models.Model):
    question=models.CharField(max_length=100)
    option_a=models.CharField(max_length=80)
    option_b=models.CharField(max_length=80)
    option_c=models.CharField(max_length=80)
    option_d=models.CharField(max_length=80)
    answer=models.CharField(max_length=80)
    def __str__(self) :
        return self.question

class quizappUsers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
