
from django.urls import path
from .views import google_news_feed  # Import your view
from .views import fact_check_feed, fake_or_what
urlpatterns = [
    path('', google_news_feed, name='home'),
    path('fact-check/', fact_check_feed, name='fact_check'),
    path('fake_or_what/', fake_or_what, name='fake_or_what')
]  
