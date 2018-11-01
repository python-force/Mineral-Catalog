from django.shortcuts import render, get_object_or_404
from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals':minerals})


def detail(request, pk):
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