from django.views.generic import ListView, CreateView, DetailView, TemplateView, RedirectView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *


class BaseView(TemplateView):
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


class CompanyPanelView(ListView):
    model = Company
    template_name = "snapvisite/company_panel.html"

    def get_queryset(self):
        user = self.request.user
        return Company.objects.filter(owner=user)


class YourCompanyView(DetailView):
    model = Company
    template_name = "snapvisite/your_company.html"

    def get_context_data(self, **kwargs):
        context = super(YourCompanyView, self).get_context_data(**kwargs)
        id_company = self.kwargs["pk"]
        context["schedule_list"] = Schedule.objects.filter(company__id=id_company)
        return context




class EditCompanyNameView(UpdateView):
    model = Company
    form_class = UpdateCompanyNameForm
    template_name = "snapvisite/company_editor.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("snapvisite:your_company", kwargs={"pk": pk})


class EditCompanyPhotoView(UpdateView):
    model = Company
    form_class = UpdateCompanyPhotoForm
    template_name = "snapvisite/company_editor.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("snapvisite:your_company", kwargs={"pk": pk})


class EditCompanyDescriptionView(UpdateView):
    model = Company
    form_class = UpdateCompanyDescriptionForm
    template_name = "snapvisite/company_editor.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("snapvisite:your_company", kwargs={"pk": pk})


class CreateAddressView(CreateView):
    model = Address
    form_class = AddressForm
    template_name = 'snapvisite/address.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.company_id = self.kwargs['company_id']
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('snapvisite:your_company', kwargs={"pk": form.instance.company_id}))


class UpdateAddressView(UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'snapvisite/company_editor.html'

    def get_success_url(self):
        company_id = self.kwargs['company_id']
        return reverse('snapvisite:your_company', kwargs={"pk": company_id})


def schedule_view(request, company_id):
    company = Company.objects.get(pk=company_id)

    if request.method == 'POST':
        formset = ScheduleInlineFormset(request.POST, instance=company)
        if formset.is_valid():
            formset.save()
            return redirect('snapvisite:your_company', pk=company.id)
    formset = ScheduleInlineFormset(instance=company)
    return render(request, 'snapvisite/schedule.html', {'formset': formset})
