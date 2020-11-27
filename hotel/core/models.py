from django.db import models

# Create your models here.
class proom(models.Model):
    img=models.ImageField(upload_to='media')
    price=models.IntegerField()
    service=models.CharField(max_length=70,default='s')

class Contact(models.Model):
    name=models.CharField(max_length=70)
    phone=models.IntegerField()
    email=models.EmailField(max_length=50)
    message=models.TextField()

class Reserve(models.Model):
    Adate=models.DateField()
    ddate=models.DateField()
    room=models.IntegerField()
    guest=models.IntegerField() 
    email=models.EmailField(max_length=50)   