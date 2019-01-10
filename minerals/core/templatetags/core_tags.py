import string
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

@register.inclusion_tag('base-alphabet.html')
def mineral_alphabet(**kwargs):
    """Mineral Alphabet"""
    alphabet = list(string.ascii_lowercase)
    return {'alphabet':alphabet, 'current_letter': kwargs['current_letter']}

@register.inclusion_tag('base-group.html')
def mineral_groups(**kwargs):
    """Mineral Groups"""
    groups = Mineral.objects.values('group').distinct()
    return {'groups':groups, 'current_group': kwargs['current_group']}

@register.inclusion_tag('base-category.html')
def mineral_category(**kwargs):
    """Mineral Category"""
    all_categories = Mineral.objects.values('category').distinct()
    return {'all_categories':all_categories, 'current_category': kwargs['current_category']}

@register.simple_tag
def get_verbose_field_name(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name.title()