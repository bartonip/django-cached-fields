from django.db import models
from cached_fields.fields import CachedIntegerField
from cached_fields.mixins import CachedFieldsMixin
from .handlers import InvoiceSignalHandler

class Item(models.Model):
    name = models.CharField(max_length=12)
    price = models.IntegerField()

class Invoice(models.Model):
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    total = CachedIntegerField(InvoiceSignalHandler().as_handler())