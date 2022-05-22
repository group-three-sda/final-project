import datetime
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, View
from django.shortcuts import render
from .forms import RegistrationProfileForm, UpdateProfileForm, GoToForm
from .models import Profile
from snapvisite.models import Appointment



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


class TimeTableView(View):
    form_class = GoToForm
    date_format = "%Y-%m-%d"

    template_name = 'account/timetable.html'

    def get(self, request, *args, **kwargs):
        option = self.kwargs["option"]
        on_screen_date = self.kwargs["data"]

        if option == "actual":
            context = generate_content(get_today())
            return render(request, "account/timetable.html", context)

        elif option == "previous":
            date = datetime.datetime.strptime(on_screen_date, self.date_format)
            previous_week = date - datetime.timedelta(days=7)
            context = generate_content(previous_week)
            return render(request, "account/timetable.html", context)

        elif option == "next":
            date = datetime.datetime.strptime(on_screen_date, self.date_format)
            next_week = date + datetime.timedelta(days=7)
            context = generate_content(next_week)
            return render(request, "account/timetable.html", context)

        else:
            context = generate_content(get_today())
            return render(request, "account/timetable.html", context)

    def post(self, request, *args, **kwargs):
        date_form = self.form_class(request.POST)
        if date_form.is_valid():
            searched_date = date_form.cleaned_data["searched_date"]
            date = datetime.datetime.strptime(searched_date, self.date_format)
            context = generate_content(date)
            return render(request, "account/timetable.html", context)
        else:
            context = generate_content(get_today())
            return render(request, "account/timetable.html", context)
