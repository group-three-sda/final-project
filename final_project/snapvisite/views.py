from django.views.generic import ListView
from .models import Category


class BaseView(ListView):
    model = Category
    template_name = "snapvisite/base.html"
