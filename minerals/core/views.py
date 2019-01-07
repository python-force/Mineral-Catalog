import string
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Mineral
from django.db.models import Q


def search(request):
    """Quering Minerals based on search"""
    term = request.GET.get('q')
    text = request.GET.get('text')
    group = request.GET.get('group')
    category = request.GET.get('category')
    if term:
        minerals = get_list_or_404(Mineral, name__istartswith=term)
    elif group:
        group = group.lower().title()
        minerals = get_list_or_404(Mineral, group=group)
        # minerals = Mineral.objects.filter(group=group).values('group')
    elif category:
        category = category.lower().title()
        minerals = get_list_or_404(Mineral, category__icontains=category)
    elif text:
        text = text.lower().title()
        # minerals = get_list_or_404(Mineral, name=text)
        minerals = Mineral.objects.filter(
            Q(name__icontains=text) |
            Q(image_caption__icontains=text) |
            Q(image_filename=text) |
            Q(category__icontains=text) |
            Q(formula__icontains=text) |
            Q(strunz_classification__icontains=text) |
            Q(color__icontains=text) |
            Q(crystal_system__icontains=text) |
            Q(unit_cell__icontains=text) |
            Q(crystal_symmetry__icontains=text) |
            Q(cleavage__icontains=text) |
            Q(mohs_scale_hardness__icontains=text) |
            Q(luster__icontains=text) |
            Q(streak__icontains=text) |
            Q(diaphaneity__icontains=text) |
            Q(optical_properties__icontains=text) |
            Q(refractive_index__icontains=text) |
            Q(refractive_index__icontains=text) |
            Q(crystal_habit__icontains=text) |
            Q(specific_gravity__icontains=text) |
            Q(group__icontains=text)
        )
    else:
        minerals = Mineral.objects.all()
    alphabet = list(string.ascii_lowercase)
    return render(request, 'index.html', {'minerals': minerals,
                                          'alphabet': alphabet,
                                          'term': term})


def index(request):
    """Load all minerals"""
    minerals = Mineral.objects.all()
    alphabet = list(string.ascii_lowercase)
    return render(request, 'index.html', {'minerals': minerals,
                                          'alphabet': alphabet})


def detail(request, pk):
    """
    Get 1 mineral based on primary key
    Create a dictionary for fields (verbose names)
    and fields values.
    """
    mineral = get_object_or_404(Mineral, pk=pk)
    field_names = []
    for field in mineral._meta.fields:
        if str(field).split(".")[2] not in ("id",
                                            "pub_date",
                                            "image_filename"):
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

    return render(request, 'detail.html', {'mineral': mineral,
                                           'mineral_dict': mineral_dict})
