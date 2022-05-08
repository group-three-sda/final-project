from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from account.models import Profile
from datetime import datetime


class Address(models.Model):
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=6)
    street_name = models.CharField(max_length=50)
    street_number = models.CharField(max_length=50)
    apartment_number = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

    def __str__(self):
        return f'({self.city} {self.street_name} {self.street_number})'


class Category(models.Model):
    category_name = models.CharField(max_length=40)
    photo = models.ImageField(blank=True, null=True, upload_to='category_image')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.category_name}'


class Company(models.Model):
    company_name = models.CharField(max_length=128)
    photo = models.ImageField(blank=True, null=True, upload_to='company_photo/')
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return f'{self.company_name}'


class CompanyDay(models.Model):
    date = models.DateField()
    company = models.OneToOneField(Company, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'companyday'
        verbose_name_plural = 'companydays'

    def __str__(self):
        return f'({self.company} {self.date})'


class Schedule(models.Model):
    day_of_week = models.CharField(max_length=20)
    open_time = models.TimeField()
    close_time = models.TimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'schedule'
        verbose_name_plural = 'schedules'

    def __str__(self):
        return f'{self.company} {self.day_of_week}'


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return f'{self.name}'


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=True)
    company_day = models.ForeignKey(CompanyDay, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'timeslot'
        verbose_name_plural = 'timeslots'

    def __str__(self):
        return f'({self.company_day.company_name};\
         [Available: {self.status} Id: {self.pk}]; ({self.start_time} - {self.end_time}))'


class Appointment(models.Model):
    note = models.CharField(max_length=128)
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'

    def __str__(self):
        return f'(Id: {self.pk} {self.user})'
