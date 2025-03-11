# homepage/urls.py

from django.urls import path
from homepage import views  # Import the views from the homepage app

urlpatterns = [
    path('', views.home, name='home'),  # Maps the base URL of homepage to the home view
]
