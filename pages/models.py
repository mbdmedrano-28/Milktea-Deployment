from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=20)
    subname = models.CharField(max_length=20)
    classname = models.CharField(max_length=30)
    price_medium = models.IntegerField()
    price_large = models.IntegerField()
    image = models.ImageField(upload_to='menu')
    bgcolor = models.CharField(max_length=20)
    offer = models.BooleanField(default=True)


class Cart(models.Model):
    username = models.CharField(max_length=30)
    item_ind = models.CharField(max_length=7)
    item_check = models.CharField(max_length=20)
    item_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    size = models.CharField(max_length=10)
    price = models.PositiveIntegerField()


class Orders(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    mode = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    flavor = models.CharField(max_length=50)
    size = models.CharField(max_length=15)
    price = models.PositiveIntegerField()
    status =models.CharField(max_length=50)
