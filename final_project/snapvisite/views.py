from django.views.generic import ListView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Category, Company
from .forms import CreateCompanyFirstStepForm


class BaseView(ListView):
    model = Category
    template_name = "snapvisite/base.html"


class CreateCompanyFirstStepView(CreateView):
    """
    First step to create a company.
    Current logged user can name and select categories for his company.
    """
    model = Company
    form_class = CreateCompanyFirstStepForm
    template_name = 'snapvisite/create_company_first_step.html'

    def form_valid(self, form):
        """
        In creator company owner always be current logged user.
        """
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        obj = form.save_m2m()
        return HttpResponseRedirect(reverse_lazy('snapvisite:home-page'))

