from django.urls import path
from .views import CreateProfileView, LoginView

app_name = 'account'

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
]
