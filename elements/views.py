from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'html/index.html', {})

def Temp(request):
    return render(request, 'html/temp.html', {})

def Form(request):
    return render(request, 'html/form.html', {})

def Abilities(request):
    return render(request, 'html/elements/abilities.html', {})

def Counter(request):
    return render(request, 'html/elements/counter.html', {})

def Heal(request):
    return render(request, 'html/elements/healing.html', {})

def Intel(request):
    return render(request, 'html/elements/intel.html', {})

def Recomb(request):
    return render(request, 'html/elements/recombulate.html', {})

def Soulsteal(request):
    return render(request, 'html/elements/soulsteal.html', {})

def Survive(request):
    return render(request, 'html/elements/survive.html', {})