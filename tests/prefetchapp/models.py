from django.db import models
from cached_fields.fields import CachedIntegerField
from cached_fields.mixins import CachedFieldsMixin
from prefetchapp.handlers import OrderSummaryCacheHandler

class OrderSummary(models.Model):
    total = CachedIntegerField(OrderSummaryCacheHandler, null=True)

class Service(models.Model):
    total = models.IntegerField()
    order = models.ForeignKey(OrderSummary, related_name="services")
    
    