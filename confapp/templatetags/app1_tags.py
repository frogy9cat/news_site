from django import template
from confapp.models import Category1
from django.db.models import Count


register = template.Library()

@register.simple_tag()
def get_category():
    return Category1.objects.annotate(Count('news'))