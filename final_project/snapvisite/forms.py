from django import forms
from django.forms import inlineformset_factory
from .models import *
from account.models import Profile


class CreateCompanyFirstStepForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'category')

    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('company',)

    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    street_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    street_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    apartment_number = forms.CharField(required=False,
                                       widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))


class UpdateCompanyNameForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name',)

    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))


class UpdateCompanyDescriptionForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('description',)

    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 5}))


class UpdateCompanyPhotoForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('photo',)

    widgets = {
        'photo': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
    }


time_widget = forms.TimeInput(attrs={'class': 'timepicker'})


class ScheduleDayForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('day_of_week', 'open_time', 'close_time')
    open_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}))
    close_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}))


ScheduleInlineFormset = inlineformset_factory(
    Company,
    Schedule,
    form=ScheduleDayForm,
    extra=7,
    max_num=7,
    can_delete=False,
)


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ('company',)

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 3}))
    time = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg', 'min': '15',
                                                              'placeholder': "Put time in minutes. Like '60' = 1h,"
                                                                             " '30' = 30min, '90' = 1h 30min"}))
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg',
                                                               'placeholder': 'Use only full numbers like: 10.00, 15,'
                                                                              ' 25.00, 25 ',
                                                               'step': 1}))


