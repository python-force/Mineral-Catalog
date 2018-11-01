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