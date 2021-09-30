from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

def first_eight_upper(value):
    '''''This is my own filter'''
    result=value[:8].upper()
    return result



register.filter('f8upper',first_eight_upper)