from django.shortcuts import render
from .models import Mineral

def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals':minerals})

def detail(request, pk):
    mineral = Mineral.objects.get(pk=pk)
    return render(request, 'detail.html', {'mineral':mineral})