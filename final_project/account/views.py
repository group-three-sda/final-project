from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView
from .forms import RegistrationProfileForm
from .models import Profile
# Create your views here.


class CreateProfileView(CreateView):
    form_class = RegistrationProfileForm
    template_name = 'account/registration_form.html'
    success_url = reverse_lazy('snapvisite:home-page')
