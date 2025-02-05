from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'learnCastellinaev1/index.html')
def about(request):
    return render(request, 'learnCastellinaev1/about.html')
def galeria(request):
    return render(request, 'learnCastellinaev1/galeria.html')
def contact(request):
    return render(request, 'learnCastellinaev1/contact.html')