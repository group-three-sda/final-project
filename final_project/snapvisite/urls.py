from django.urls import path
from .views import BaseView

urlpatterns = [
    path('snapvisite/home-page/', BaseView.as_view())
]
