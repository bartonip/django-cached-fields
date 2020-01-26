from django.test import TestCase

from unittest.mock import MagicMock, patch

from someapp.models import Invoice

from datetime import datetime

from cached_fields.exceptions import UnauthorisedChange

# Create your tests here.

class TestTriggers(TestCase):
    def test_calculationOccursOnCreationTrigger(self):
        invoice = Invoice.objects.create(quantity=2, amount=3)
        self.assertEqual(invoice.total, 6)

    def test_calculationOccursOnFieldChangeTrigger(self):
        invoice = Invoice.objects.create(quantity=2, amount=3)
        invoice.quantity = 3
        invoice.save()
        self.assertEqual(invoice.total, 9)

class TestEditingField(TestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(quantity=2, amount=3)
    
    def test_shouldFail_whenDirectModificationMadeToCache(self):
        self.invoice.total = 12941924
        with self.assertRaises(UnauthorisedChange):
            self.invoice.save()
        
    def test_shouldFail_whenValueSpecifiedForCacheOnCreate(self):
        with self.assertRaises(UnauthorisedChange):
            invoice = Invoice.objects.create(quantity=3, amount=4, total=12)
        

class TestTimestampUpdates(TestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(quantity=2, amount=3)

    def test_modelHasAttr(self):
        self.assertEqual(self.invoice.total_last_updated, datetime(2019,1,1,1,2))
        