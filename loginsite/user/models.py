from django.db import models

# Create your models here.


class User(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)