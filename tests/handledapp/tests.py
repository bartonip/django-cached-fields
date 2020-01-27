from django.test import TestCase

from unittest.mock import MagicMock, patch

from handledapp.models import Invoice, Item
from handledapp.handlers import InvoiceSignalHandler

from datetime import datetime

from cached_fields.exceptions import UnauthorisedChange

# Create your tests here.

class TestCalculationOnCreate(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="ARSE", price=3)

    def test_cacheIsInitialisedWhenModelCreated(self):
        invoice = Invoice.objects.create(item=self.item, quantity=99)
        self.assertEqual(invoice.total, 9)


# class TestTriggers(TestCase):
#     def setUp(self):
#         self.item = Item.objects.create(name="ARSE", price=3)
#         self.invoice = Invoice(item=self.item, quantity=3)
#         self.invoice.save()
        
    
#     def test_What(self):
#         self.invoice.save()
#         self.assertEqual(self.invoice.total,9)