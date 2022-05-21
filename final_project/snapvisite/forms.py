from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from .models import Company, Category, Address, Schedule, Service, CompanyDay, TimeSlot, Appointment


class CreateCompanyFirstStepForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'category')

    company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )


class EditCategoriesForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('category',)

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

    def clean(self):
        cleaned_data = super().clean()
        city = cleaned_data.get("city")
        if not city[0].isupper():
            raise ValidationError({"city": "First letter of city had to be uppercase."})


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
        
    open_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}))
    close_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}))



ScheduleInlineFormset = inlineformset_factory(
    Company,
    Schedule,
    form=ScheduleDayForm,
    extra=7,
    max_num=7,
    can_delete=True,
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


class ContactForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('phone_number', 'email')

    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


class CompanyDayForm(forms.ModelForm):
    class Meta:
        model = CompanyDay
        exclude = ('company',)
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': f'You cant duplicate your working days.'
            }
        }

    date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))


class CompanyTimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ('start_time',)

    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}))


class CompanyTimeSlotMultipleForm(forms.Form):
    from_time = forms.TimeField(label="Start Time", widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}))
    to_time = forms.TimeField(label="End Time", widget=forms.TimeInput(attrs={'class': 'form-control timepicker'}))
    delta = forms.IntegerField(label="Time step(in minutes)",
                               widget=forms.NumberInput(attrs={
                                   'class': 'form-control form-control-lg',
                                   'placeholder': 'Enter minutes. What step to create a new slot.'
                               }))

    def clean(self):
        cleaned_data = super().clean()
        from_time = cleaned_data.get("from_time")
        to_time = cleaned_data.get("to_time")

        if from_time > to_time:
            raise ValidationError({"to_time": "Start time have to be lower than end time"})



class CreateAppointmentForm(forms.ModelForm):
    CHOICES = [(True, 'Pay with card now.'), (False, 'Pay by cash on visit.')]

    class Meta:
        model = Appointment
        fields = ('note', 'payment_status')

    note = forms.CharField(label='Additional information', widget=forms.Textarea(
        attrs={'class': 'form-control form-control-lg', 'rows': 3}))
    payment_status = forms.ChoiceField(label='Payment option', widget=forms.RadioSelect, choices=CHOICES)
