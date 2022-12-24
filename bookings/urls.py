# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal:
from bookings import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Urls for all the pages in the bookings app
urlpatterns = [
    path('bookings/', views.AllClubs.as_view(), name='golf_clubs'),
    path('<slug:slug>/', views.ClubExpand.as_view(), name='club_expand'),
]
