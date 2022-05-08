from django.urls import path
from .views import CreateProfileView, DetailProfileView, UpdateProfileView

app_name = 'account'

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='registration'),
    path('profile-detail/<int:pk>/', DetailProfileView.as_view(), name='profile_detail'),
    path('profile-edit/<int:pk>/', UpdateProfileView.as_view(), name='profile_edit')
]
