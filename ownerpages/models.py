from django.db import models


class Slot(models.Model):
    slot_ind = models.CharField(max_length=20)
    nameType = models.CharField(max_length=10)
    name_unique = models.CharField(max_length=20)
    quanType = models.CharField(max_length=10)
    quantity_unique = models.IntegerField()
    unitType = models.CharField(max_length=10)
    unit_unique = models.CharField(max_length=20)


class Sales(models.Model):
    today_date = models.DateField(verbose_name="date", auto_now_add=True)
    today_sale = models.IntegerField()


