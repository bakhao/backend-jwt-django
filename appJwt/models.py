from time import timezone

from django.db import models


# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    email = models.CharField(max_length=60)


class Book(models.Model):
    author = models.CharField(max_length=60)
    title = models.CharField(max_length=60)


