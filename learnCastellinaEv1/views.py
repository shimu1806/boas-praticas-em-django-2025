from django.shortcuts import render
from .models import Local

# Create your views here.

def home(request):
    return render(request, 'learnCastellinaev1/index.html')

def about(request):
    return render(request, 'learnCastellinaev1/about.html')

def cosa_per_fare(request):
    # Filtra apenas locais habilitados para exibição
    locais = Local.objects.filter(habilitado=True).order_by('nome')
    
    return render(request, 'learnCastellinaev1/cosa-per-fare.html', {'locais': locais})

def galeria(request):
    return render(request, 'learnCastellinaev1/galeria.html')

def contact(request):
    return render(request, 'learnCastellinaev1/contact.html')