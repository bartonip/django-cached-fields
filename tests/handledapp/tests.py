from django.test import TestCase

from unittest.mock import MagicMock, patch

from handledapp.models import Invoice, Item
from handledapp.handlers import InvoiceSignalHandler

from datetime import datetime

from cached_fields.exceptions import UnauthorisedChange
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your tests here.

class TestTriggers(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="ARSE", price=3)
        self.invoice = Invoice(item=self.item, quantity=3)
        self.invoice.cache_toolchain.set_cache_value('total', 9)
        self.invoice.save()
        
    
    def test_What(self):

        self.assertEqual(1,2)