from django.test import TestCase

from unittest.mock import MagicMock, patch

from handledapp.models import Invoice, Item, Carrot
from handledapp.handlers import InvoiceSignalHandler

from datetime import datetime

from cached_fields.exceptions import UnauthorisedChange
from cached_fields.handlers import CachedFieldSignalHandler

# Create your tests here.

class TestCalculationOnCreate(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="ARSE", price=3)

    def test_cacheIsInitialisedWhenModelCreated(self):
        invoice = Invoice.objects.create(item=self.item, quantity=99)
        self.assertEqual(invoice.total, 297)
        invoice.quantity = 3
        invoice.save()
        self.assertEqual(invoice.total, 9)
    
    def test_cacheIsInitialisedWhenModelInitialisedAndSaved(self):
        invoice = Invoice(item=self.item, quantity=99)
        invoice.save()
        self.assertEqual(invoice.total, 297)
        invoice.quantity = 3
        invoice.save()
        self.assertEqual(invoice.total, 9)

class TestUpdateMultiply(TestCase):
    pass

class TestUpdateSQLKeyword(TestCase):
    pass

class TestMultipleCachedFieldsOnModel(TestCase):
    def setUp(self):
        pass

    def test_multipleCachedFields_shouldUpdateWhenSaved(self):
        carrot = Carrot.objects.create(value_one=2, value_two=11)
        self.assertEqual(carrot.multiple, 22)
        self.assertEqual(carrot.addition, 13)

# class TestTriggers(TestCase):
#     def setUp(self):
#         self.item = Item.objects.create(name="ARSE", price=3)
#         self.invoice = Invoice(item=self.item, quantity=3)
#         self.invoice.save()
        
    
#     def test_What(self):
#         self.invoice.save()
#         self.assertEqual(self.invoice.total,9)