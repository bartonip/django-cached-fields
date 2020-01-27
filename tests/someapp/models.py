from django.db import models
from cached_fields.fields import CachedIntegerField
from cached_fields.mixins import CachedFieldsMixin

def calc_total(instance):
    return instance.amount * instance.quantity

class Invoice(models.Model):
    amount = models.IntegerField()
    quantity = models.IntegerField()
    total = CachedIntegerField(calc_total, field_triggers=['amount', 'quantity'])