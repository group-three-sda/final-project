from django.views.generic import ListView, CreateView, DetailView, TemplateView, RedirectView, UpdateView, View
from django.http import HttpResponseRedirect, HttpResponseBadRequest
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
        return HttpResponseRedirect(reverse_lazy('snapvisite:company_panel'))


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
        """
        Send a schedule and service list to view
        """
        context = super(YourCompanyView, self).get_context_data(**kwargs)
        id_company = self.kwargs["pk"]
        context["schedule_list"] = Schedule.objects.filter(company__id=id_company)
        context["services_list"] = Service.objects.filter(company__id=id_company)
        return context


class EditCompanyNameView(UpdateView):
    """ EDITOR """
    model = Company
    form_class = UpdateCompanyNameForm
    template_name = "snapvisite/company_editor.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("snapvisite:your_company", kwargs={"pk": pk})


class EditCompanyPhotoView(UpdateView):
    """ EDITOR """
    model = Company
    form_class = UpdateCompanyPhotoForm
    template_name = "snapvisite/company_editor.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("snapvisite:your_company", kwargs={"pk": pk})


class EditCompanyDescriptionView(UpdateView):
    """ EDITOR """
    model = Company
    form_class = UpdateCompanyDescriptionForm
    template_name = "snapvisite/company_editor.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("snapvisite:your_company", kwargs={"pk": pk})


class EditCompanyCategoriesView(UpdateView):
    """ EDITOR """
    model = Company
    form_class = EditCategoriesForm
    template_name = "snapvisite/company_editor.html"

    def form_valid(self, form, *args, **kwargs):
        form.save(commit=False)
        form.save()
        form.save_m2m()
        id_company = self.kwargs["pk"]
        return HttpResponseRedirect(reverse('snapvisite:your_company', kwargs={"pk": id_company}))


class CreateAddressView(CreateView):
    """ EDITOR """
    model = Address
    form_class = AddressForm
    template_name = 'snapvisite/address.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.company_id = self.kwargs['company_id']
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('snapvisite:your_company', kwargs={"pk": form.instance.company_id}))


class UpdateAddressView(UpdateView):
    """ EDITOR """
    model = Address
    form_class = AddressForm
    template_name = 'snapvisite/address.html'

    def get_success_url(self):
        company_id = self.kwargs['company_id']
        return reverse('snapvisite:your_company', kwargs={"pk": company_id})


class ScheduleView(View):
    """ EDITOR """
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        formset = ScheduleInlineFormset(instance=company)
        return render(request, 'snapvisite/schedule.html', {'formset': formset})

    def post(self, request, company_id, **kwargs):
        company = Company.objects.get(pk=company_id)
        formset = ScheduleInlineFormset(request.POST, instance=company)
        if formset.is_valid():
            formset.save()
            return redirect('snapvisite:your_company', pk=company.id)


class CreateServiceView(CreateView):
    """ EDITOR """
    model = Service
    form_class = ServiceForm
    template_name = 'snapvisite/company_editor.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.company_id = self.kwargs['company_id']
        obj = form.save(commit=False)
        obj.save()
        return HttpResponseRedirect(reverse('snapvisite:your_company', kwargs={"pk": form.instance.company_id}))


class UpdateServiceView(UpdateView):
    """ EDITOR """
    model = Service
    form_class = ServiceForm
    template_name = 'snapvisite/company_editor.html'

    def get_success_url(self):
        company_id = self.kwargs['company_id']
        return reverse('snapvisite:your_company', kwargs={"pk": company_id})


class CompanyListView(ListView):
    model = Company
    template_name = "snapvisite/company_list.html"

    def get_queryset(self):
        return Company.objects.all()







