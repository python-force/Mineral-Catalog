import string
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Mineral


def search(request):
    """Load all minerals"""
    term = request.GET.get('q')
    minerals = get_list_or_404(Mineral, name__istartswith=term)
    alphabet = list(string.ascii_lowercase)
    return render(request, 'search.html', {'minerals':minerals, 'alphabet':alphabet, 'term':term})

def index(request):
    """Load all minerals"""
    minerals = Mineral.objects.all()
    alphabet = list(string.ascii_lowercase)
    return render(request, 'index.html', {'minerals':minerals, 'alphabet':alphabet})


def detail(request, pk):
    """
    Get 1 mineral based on primary key
    Create a dictionary for fields (verbose names)
    and fields values.
    """
    mineral = get_object_or_404(Mineral, pk=pk)
    field_names = []
    for field in mineral._meta.fields:
        if str(field).split(".")[2] not in ("id", "pub_date", "image_filename"):
            field_names.append(field.name.replace("_", " "))

    field_data = [
        mineral.name,
        mineral.image_caption,
        mineral.category,
        mineral.formula,
        mineral.strunz_classification,
        mineral.color,
        mineral.crystal_system,
        mineral.unit_cell,
        mineral.crystal_symmetry,
        mineral.cleavage,
        mineral.mohs_scale_hardness,
        mineral.luster,
        mineral.streak,
        mineral.diaphaneity,
        mineral.optical_properties,
        mineral.refractive_index,
        mineral.crystal_habit,
        mineral.specific_gravity,
        mineral.group
    ]

    mineral_dict = {}

    for i in range(0, len(mineral._meta.fields) - 3):
        mineral_dict[field_names[i]] = field_data[i]

    return render(request, 'detail.html', {'mineral':mineral, 'mineral_dict':mineral_dict})