from django.db import models

# student.
class Student(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=8)

