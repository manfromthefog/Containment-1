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
    return render(request, 'html/wither/abilities.html', {})

def Counter(request):
    return render(request, 'html/wither/counter.html', {})

def Heal(request):
    return render(request, 'html/wither/healing.html', {})

def Intel(request):
    return render(request, 'html/wither/intel.html', {})

def Recomb(request):
    return render(request, 'html/wither/recombulate.html', {})

def Soulsteal(request):
    return render(request, 'html/wither/soulsteal.html', {})

def Survive(request):
    return render(request, 'html/wither/survive.html', {})
