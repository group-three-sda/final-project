from django import template
from snapvisite.models import Company, Category

register = template.Library()


@register.simple_tag
def all_categories():
    return Category.objects.all()
