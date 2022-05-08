from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from .forms import RegistrationProfileForm, UpdateProfileForm
from .models import Profile
# Create your views here.


class CreateProfileView(CreateView):
    form_class = RegistrationProfileForm
    template_name = 'account/registration_form.html'
    success_url = reverse_lazy('snapvisite:home-page')


class DetailProfileView(DetailView):
    model = Profile


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'account/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("account:profile_detail", kwargs={"pk": pk})

