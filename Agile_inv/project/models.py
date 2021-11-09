from django.db import models
from django.contrib.postgres.fields import ArrayField

class Project(models.Model):
    name = models.CharField(max_length=200 , primary_key=True)
    teamLeader = models.CharField(max_length=200)
    date=models.DateField()
    def __str__(self):
        return self.name
# Create your models here.
class User_of_project(models.Model):
    pk_user = models.CharField(max_length=200 )
    pk_project = models.CharField(max_length=200 )
   


