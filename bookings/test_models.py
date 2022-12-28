# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
from datetime import date
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Club, Booking, User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# These test will create a new food and drink item,
# it will check the name, description and price


class TestModels(TestCase):
    def setUp(self):
        self.club = Club(
            club_id=1,
            golf_club_name='Druids Vale',
            slug='Druids-Vale'
            )
        self.user = User(
            username='Tester Test',
            email='test@aaa.com'
            )
        self.booking = Booking(
            booking_id=32,
            golf_club_name=self.club,
            user=self.user,
            player_count=6,
            created_date='2022-12-12',
            requested_date='2022-12-12',
            requested_time='12:00',
            name='Tester Test',
            phone='+353123456789',
            email='test@aaa.com',
            )
