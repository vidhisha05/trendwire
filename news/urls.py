
from django.urls import path
from .views import google_news_feed  # Import your view

urlpatterns = [
    path('', google_news_feed, name='home'),  # This should point to your view
]
