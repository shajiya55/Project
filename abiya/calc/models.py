from django.db import models

# Create your models here.
number=( 
    ("1", "1"), 
    ("2", "2"), 
    ("3", "3"), 
    ("4", "4"), 
    ("5", "5"), 
    ("6", "6"), 
    ("7", "7"), 
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),

) 
class contact(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(max_length=70)
    message=models.TextField()

class menu(models.Model):
    mlogo=models.ImageField(upload_to='media')
    mname=models.CharField(max_length=70)
    mprice=models.IntegerField()    

class table(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=70)
    phone=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    number_Of_Members=models.CharField(max_length=50,choices=number)    

class himg(models.Model):
    img =models.ImageField(upload_to='media') 