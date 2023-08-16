from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Corpusobject(models.Model):
    catid = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    knownloc = models.BooleanField()
    physical = models.NullBooleanField()
    verbsaddress = models.CharField(max_length=200, blank=True)
    downloadable = models.NullBooleanField()
    project = models.CharField(max_length=50, blank=True)
    corpustype = models.CharField(max_length=50, blank=True)
    language = models.TextField(blank=True)
