# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Club, Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Registration of Clubs to display in the admin panel
@admin.register(Club)
class ClubAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
    list_display = (
        'club_id',
        'golf_club_name',
        'slug',
        'available',
        )
    prepopulated_fields = {'slug': ('golf_club_name',)}
    search_fields = ['golf_club_name', 'description']


# Registration of bookings to display in the admin panel
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'golf_club_name',
        'email',
        'phone',
        'player_count',
        'status',
        'requested_date',
        'requested_time',
        'created_date'
        )
    list_display = (
        'booking_id',
        'user',
        'name',
        'phone',
        'player_count',
        'status',
        'golf_club_name',
        'requested_date',
        'requested_time',
        'created_date')

    search_fields = ['user__username']
    list_filter = (('requested_date', DateRangeFilter),)
    actions = ['confirm_bookings']
