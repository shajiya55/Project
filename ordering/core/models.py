from django.db import models
# Create your models here.
class limit(models.Model):
    price=models.IntegerField()
    amount=models.IntegerField()

class market(models.Model):
    Wallet=models.IntegerField()
    amount=models.IntegerField()

class stop(models.Model):
    trigger_price=models.IntegerField()
    price=models.IntegerField()
    amount=models.IntegerField()