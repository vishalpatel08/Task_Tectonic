from django.db import models

# Create your models here.

class Item(models.Model):
    itemid = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=122)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class User(models.Model):
    userid = models.CharField(max_length=10, unique=True)
    username = models.CharField(max_length=30)
    credits = models.FloatField()
    def __str__(self):
        return self.username

class Orders(models.Model):
    orderid = models.CharField(max_length=15)
    userid = models.CharField(max_length=10)
    itemid = models.CharField(max_length=12)
    name = models.CharField(max_length=122)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.userid
