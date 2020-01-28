from django.test import TestCase

from unittest.mock import MagicMock, patch

from reverseapp.models import Invoice, Item
from reverseapp.handlers import InvoiceSignalHandler

from datetime import datetime

from cached_fields.exceptions import UnauthorisedChange

class TestReverseCalculation(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name="ARSE", price=3)

    def test_cacheIsValidWhenMultipleChangesAresCreated(self):
        invoices = {}
        for i in range(1, 25):
            invoices[i] = Invoice.objects.create(quantity=i, item=self.item)
        for i, invoice in invoices.items():
            self.assertEqual(invoice.total, 3*i)
            invoice.quantity = i * 2
            invoice.save()
            self.assertEqual(invoice.total, 3*i*2)
        self.item.price=10
        self.item.save()
        for i, invoice in invoices.items():
            invoice.refresh_from_db()
            self.assertEqual(invoice.total, 10*i*2)