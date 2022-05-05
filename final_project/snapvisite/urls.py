from django.urls import path
from .views import BaseView


app_name = "snapvisite"

urlpatterns = [
    path('snapvisite/home-page/', BaseView.as_view(), name='home-page')
]
