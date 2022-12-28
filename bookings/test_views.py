# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# test that the correct views are used when requested


class TestBookingsViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.golf_clubs_url = reverse('golf_clubs')
        self.club_expand_url = reverse(
            'club_expand',
            kwargs={'slug': 'druids-vale'}
            )
        self.booking_list_url = reverse('booking_list')

    def test_all_clubs_GET(self):
        response = self.client.get(self.golf_clubs_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/golf_clubs.html')
