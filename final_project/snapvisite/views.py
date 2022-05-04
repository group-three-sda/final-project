from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = "snapvisite/base.html"
