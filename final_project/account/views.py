import datetime

from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.http import HttpResponseRedirect
from snapvisite.models import Appointment
from .utils import send_mail

from .forms import RegistrationProfileForm, UpdateProfileForm
from .models import Profile
from django.contrib.messages.views import SuccessMessageMixin


class CreateProfileView(SuccessMessageMixin, CreateView):
    form_class = RegistrationProfileForm
    template_name = 'account/registration_form.html'
    success_message = 'Your account has been created successfully.'

    def form_valid(self, form):
        username = form.cleaned_data['user_name']
        email = form.cleaned_data['email']
        send_mail(username, email)
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse_lazy('snapvisite:home-page'))


class DetailProfileView(DetailView):
    model = Profile


class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'account/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("account:profile_detail", kwargs={"pk": pk})


class CheckAppointmentsView(DetailView):
    model = Profile
    template_name = 'account/appointments.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        today = datetime.datetime.now()
        now = datetime.date(int(today.year), int(today.month), int(today.day))
        data['appointments_future'] = Appointment.objects.filter(user__id=self.kwargs["pk"],
                                                                 time_slot__company_day__date__gte=now)
        data['appointments_history'] = Appointment.objects.filter(user__id=self.kwargs["pk"],
                                                                  time_slot__company_day__date__lt=now)
        return data
