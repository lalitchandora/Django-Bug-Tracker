from django.db import models
from django import forms

class Project(models.Model):
    name = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=70)
    technology = models.CharField(max_length=50)

    def __str__(self):
        return self.name