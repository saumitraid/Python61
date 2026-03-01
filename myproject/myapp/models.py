from django.db import models

# Create your models here. 

class Student(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    city=models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)

