from django.contrib import admin
from django.urls import path, include
from .views import CreateProfileView

app_name = 'account'

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='registration')
]