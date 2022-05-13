from django import forms
from .models import Company, Category, Address
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
        apartment_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))


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
