from django.contrib import admin
from django.urls import path, include
from snapvisit.views import HomePageView

app_name = 'snapvisit'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page')
]
