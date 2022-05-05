from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegistrationProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('email', 'user_name', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_name', 'first_name', 'last_name', 'phone_number')


