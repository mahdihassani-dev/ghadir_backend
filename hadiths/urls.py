# your_app/urls.py
from django.urls import path
from .views import random_hadith

urlpatterns = [
    path('api/hadith/random/', random_hadith, name='random_hadith'),
]
