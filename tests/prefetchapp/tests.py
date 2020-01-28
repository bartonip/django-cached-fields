from django.test import TestCase

from unittest.mock import MagicMock, patch

from prefetchapp.models import Service, OrderSummary

from datetime import datetime

from cached_fields.exceptions import UnauthorisedChange

# Create your tests here.

class TestPrefechOperational(TestCase):
    def setUp(self):
        self.order = OrderSummary.objects.create()

    def test_prefetchWorks_whenParameterSpecified(self):
        for i in range(0, 20):
            service = Service.objects.create(total=i, order=self.order)
        service.save()
        self.assertEqual(self.order.total, 190)
