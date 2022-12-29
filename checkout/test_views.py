# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
# Internal:
from checkout.models import Order
from profiles.models import UserProfile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutViews(TestCase):
    """
    A class for testing the checkout app views
    """
    def setUp(self):
        """
        Create test users, regular, and superuser and a test order
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')
        test_user_superuser = User.objects.create_superuser(
            username='test_user_superuser', password='test_password')

        test_user.save()
        test_user_superuser.save()
        test_user = UserProfile.objects.get(user=test_user)

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
        Delete test orders
        """
        Order.objects.all().delete()

    def test_checkout_view_empty_cart(self):
        """
        This test test an empty cart for checkout and verifies
        """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your basket at the moment")
