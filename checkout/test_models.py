# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from .models import Order
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create a test product and order
        """

        Order.objects.create(
            full_name='Test Name',
            email='test@gmail.com',
            phone_number='123456789',
            address1='Test Address',
            address2='Test Address2',
            county='Kildare',
            country='Ireland',
            town_or_city='Test City',

        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        Order.objects.all().delete()

    def test_order_str_method(self):
        """
        This test tests the order number string
        """
        order = Order.objects.get(email='test@gmail.com')
        self.assertEqual(str(order), order.order_number)
