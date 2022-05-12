from django import forms
from .models import Company, Category
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
