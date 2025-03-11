
from django.urls import path
from .views import google_news_feed  # Import your view
from .views import fact_check_feed
urlpatterns = [
    path('', google_news_feed, name='home'),
      path('fact-check/', fact_check_feed, name='fact_check'),
]  
