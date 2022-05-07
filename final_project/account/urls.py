from django.urls import path
from .views import CreateProfileView

app_name = 'account'

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='registration'),
]
