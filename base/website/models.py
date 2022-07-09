from operator import mod
from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=10000)
    photo = models.ImageField()
    description = models.CharField(max_length=1000000)
    tech = models.CharField(max_length=10000)
    gitlink =  models.URLField()
    codelink = models.URLField()

    def __str__(self):
      return self.name

