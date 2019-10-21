from django import template

register = template.Library()


@register.filter
def upper_value(value):
    return value.upper()