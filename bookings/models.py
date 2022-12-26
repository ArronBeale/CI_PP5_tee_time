# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Restaurant first sitting at noon and last sitting 11pm
tee_times = (
    ('09:00', '09:00'),
    ('09:10', '09:10'),
    ('09:20', '09:20'),
    ('09:30', '09:30'),
    ('09:40', '09:40'),
    ('09:50', '09:50'),
    ('10:00', '10:00'),
    ('10:10', '10:10'),
    ('10:20', '10:20'),
    ('10:30', '10:30'),
    ('10:40', '10:40'),
    ('10:50', '10:50'),
    ('11:00', '11:00'),
    ('11:10', '11:10'),
    ('11:20', '11:20'),
    ('11:30', '11:30'),
    ('11:40', '11:40'),
    ('11:50', '11:50'),
    ('12:00', '12:00'),
    ('12:10', '12:10'),
    ('12:20', '12:20'),
    ('12:30', '12:30'),
    ('12:40', '12:40'),
    ('12:50', '12:50'),
    ('13:00', '13:00'),
    ('13:10', '13:10'),
    ('13:20', '13:20'),
    ('13:30', '13:30'),
    ('13:40', '13:40'),
    ('13:50', '13:50'),
    ('14:00', '14:00'),
    ('14:10', '14:10'),
    ('14:20', '14:20'),
    ('14:30', '14:30'),
    ('14:40', '14:40'),
    ('14:50', '14:50'),
    ('15:00', '15:00'),
    ('15:10', '15:10'),
    ('15:20', '15:20'),
    ('15:30', '15:30'),
    ('15:40', '15:40'),
    ('15:50', '15:50'),
    ('16:00', '16:00'),
    ('16:10', '16:10'),
    ('16:20', '16:20'),
    ('16:30', '16:30'),
    ('16:40', '16:40'),
    ('16:50', '16:50'),
)


# Status options for tee time bookings
status_options = (
    ('Tee Time Confirmed', 'Tee Time Confirmed'),
    ('Tee Time Rejected', 'Tee Time Rejected'),
    ('Tee Time Expired', 'Tee Time Expired'),
)


# The golf club model for the database


class Club(models.Model):
    """
    a class for the golf club model
    """
    club_id = models.AutoField(
        primary_key=True
        )
    golf_club_name = models.CharField(
        max_length=254,
        unique=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        default='',
        )
    description = models.CharField(
        max_length=2000,
        unique=True)
    available = models.BooleanField(
        default=True
        )
    image = models.ImageField(
        upload_to='clubs/',
        null=True,
        blank=True
        )
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ['golf_club_name']

    def __str__(self):
        return self.golf_club_name


# The booking model for users to book tee times


class Booking(models.Model):
    """
    a class for the Booking model
    """
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=25,
        choices=tee_times,
        default='12:00'
        )
    golf_club_name = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        related_name="club_name",
        null=True
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    phone = PhoneNumberField(null=True)
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='Tee Time Confirmed'
        )
    players = (
        (1, "1 Player"),
        (2, "2 Players"),
        (3, "3 Players"),
        (4, "4 Players"),
        )
    player_count = models.IntegerField(choices=players, default=1)

    # class Meta:
    #     ordering = ['-requested_time']
    #     unique_together = ('requested_date', 'requested_time', 'golf_club_name')

    def __str__(self):
        return self.status
