from django import template
import random

from minerals.core.models import Mineral

register = template.Library()

@register.inclusion_tag('base-random.html')
def random_mineral():
    """Random Mineral"""
    minerals = Mineral.objects.all()
    mineral = random.choice(minerals)
    return {'mineral':mineral}

@register.inclusion_tag('base-group.html')
def mineral_groups():
    """Random Mineral"""
    groups = Mineral.objects.values('group').distinct()
    return {'groups':groups}

@register.simple_tag
def get_verbose_field_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()