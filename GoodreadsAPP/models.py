from django.db import models
from django import forms

class input(models.Model):
    username = models.CharField(max_length=2000)
    password = models.CharField(max_length=2000)
    booklist = models.CharField(max_length=2000)

class recommendationForm(models.Model):
    username = models.CharField(max_length=2000)
    password = models.CharField(max_length=2000)

class findLibrary(models.Model):
    location = models.CharField(max_length=2000)

