from django import template
from snapvisite.models import Company, Category

register = template.Library()


@register.simple_tag
def all_categories():
    return Category.objects.all()


@register.filter('duration_format')
def duration_format(value):
    h = 'h'
    m = 'min'
    hours = int(value/60)
    minutes = value % 60

    if hours == 0:
        return f'{minutes}{m}'
    else:
        return f'{hours}{h}{minutes}{m}'


