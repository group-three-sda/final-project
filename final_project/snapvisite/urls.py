from django.urls import path
from .views import *


app_name = "snapvisite"

urlpatterns = [
    path('snapvisite/home-page/', BaseView.as_view(), name='home-page'),
    path('snapvisite/create-company/', CreateCompanyFirstStepView.as_view(), name='create_company_first_step'),
    path('snapvisite/company-panel/', CompanyPanelView.as_view(), name='company_panel'),
    path('snapvisite/your-company/<int:pk>/', YourCompanyView.as_view(), name='your_company'),
    path('snapvisite/change-company-name/<int:pk>/', EditCompanyNameView.as_view(), name='company_name_edit'),
    path('snapvisite/change-company-description/<int:pk>/', EditCompanyDescriptionView.as_view(),
         name='company_desc_edit'),
    path('snapvisite/change-company-photo/<int:pk>/', EditCompanyPhotoView.as_view(), name='company_photo_edit')
]
