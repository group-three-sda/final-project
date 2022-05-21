from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile


class RegistrationProfileForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('email', 'user_name', 'password1', 'password2')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'example:.. +48 123 456 789'}),
        }


#class PasswordChangeCustomForm(PasswordChangeForm):
#    error_css_class = 'has-error'
#    error_messages = {'password_incorrect': "The old password is not correct. Try again."}
#    old_password = forms.CharField(required=True, label='Password', widget=forms.PasswordInput(attrs={
#                    'class': 'form-control'}),
#                  error_messages={
#                    'required': 'The password can not be empty'})
#    new_password1 = forms.CharField(required=True, label='New password', widget=forms.PasswordInput(attrs={
#                    'class': 'form-control'}),
#                  error_messages={
#                    'required': 'The password can not be empty'})
#    new_password2 = forms.CharField(required=True, label='New password', widget=forms.PasswordInput(attrs={
#                    'class': 'form-control'}),
#                  error_messages={
#                    'required': 'The password can not be empty'})
