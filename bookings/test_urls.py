# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from bookings.views import (BookingList,
                            EditBooking, cancel_booking, AllClubs)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Test that all the correct urls are used when requested


class BookingsUrls(SimpleTestCase):
    """
    This class is for testing the bookings app
    urls
    """
    def test_all_clubs_resolved(self):
        url = reverse('golf_clubs')
        self.assertEquals(resolve(url).func.view_class, AllClubs)

    def test_booking_list_resolved(self):
        url = reverse('booking_list')
        self.assertEquals(resolve(url).func.view_class, BookingList)

    def test_edit_booking_url_resolved(self):
        url = reverse('edit_booking', args=['1'])
        self.assertEquals(resolve(url).func.view_class, EditBooking)

    def test_cancel_booking_url_resolved(self):
        url = reverse('cancel_booking', args=['1'])
        self.assertEquals(resolve(url).func, cancel_booking)
