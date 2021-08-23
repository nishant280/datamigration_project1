from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=200, default='Address Here')
    number=models.CharField(max_length=10)
    gender=models.CharField(max_length=5,default='M or F')