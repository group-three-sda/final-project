from django.urls import path
from .views import CheckAppointmentsView, CreateProfileView, DetailProfileView, UpdateProfileView, TimeTableView
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

app_name = 'account'

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='registration'),
    path('password_change_form/', auth_views.PasswordChangeView.as_view(template_name='account/password_change_form.html', success_url=reverse_lazy('account:password-change-done')), name='password-change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password-change-done'),
    path('profile-detail/<int:pk>/', DetailProfileView.as_view(), name='profile_detail'),
    path('profile-edit/<int:pk>/', UpdateProfileView.as_view(), name='profile_edit'),
    path('company/timetable/<str:option>/<str:data>/', TimeTableView.as_view(), name='timetable'),
    path('appointment-profile/<int:pk>/', CheckAppointmentsView.as_view(), name='appointments_user')
]
