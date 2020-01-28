from django.db import models
from cached_fields.fields import CachedIntegerField
from cached_fields.mixins import CachedFieldsMixin
from .handlers import InvoiceSignalHandler, CarrotAdditionHandler, CarrotMultipleHandler

class Item(models.Model):
    name = models.CharField(max_length=12)
    price = models.IntegerField()

class Invoice(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = CachedIntegerField(InvoiceSignalHandler)

class Carrot(models.Model):
    value_one = models.IntegerField()
    value_two = models.IntegerField()
    multiple = CachedIntegerField(CarrotMultipleHandler)
    addition = CachedIntegerField(CarrotAdditionHandler)