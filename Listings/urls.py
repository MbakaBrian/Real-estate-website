from django.urls import path
from . import views

urlpatterns = [
    path('create_listing/', views.add_listing, name='CreateListing'),
    path('listingsPage/', views.listingsPage, name='listingsPage'),
]