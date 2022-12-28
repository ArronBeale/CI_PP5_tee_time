# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase

# Internal:
from .forms import OrderForm

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutForms(TestCase):
    """
    A class for testing checkout forms
    """

    def test_add_order_form(self):
        """
        This test tests the order form object
        """
        form = OrderForm({
            'full_name': 'test name',
            'email': 'test@aaa.com',
            'phone_number': '123456',
            'address1': 'test address 1',
            'address2': 'test address 2',
            'town_or_city': 'test city',
            'postcode': '12345',
            'country': 'Ireland',
            'county': 'Test County',
        })
