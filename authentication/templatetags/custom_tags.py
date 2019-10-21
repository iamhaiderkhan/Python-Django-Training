from django import template

register = template.Library()


@register.filter
def upper(value):
    return value.upper()