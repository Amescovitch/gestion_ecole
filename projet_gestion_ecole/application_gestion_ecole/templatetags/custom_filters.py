# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='get_by_eleve')
def get_by_eleve(queryset, eleve):
    try:
        return queryset.get(eleve=eleve)
    except queryset.model.DoesNotExist:
        return None
