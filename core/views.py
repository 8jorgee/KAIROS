from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

@login_required
def registros(request):
    return render(request, 'core/registros.html')

@login_required
def historial(request):
    return render(request, 'core/historial.html')

@login_required
def PLC(request):
    return render(request, 'core/PLC.html')

@login_required
def materia_prima(request):
    return render(request, 'core/materia_prima.html')

@login_required
def experimento(request):
    return render(request, 'core/experimentos.html')

@login_required
def confrontar(request):
    return render(request, 'core/confrontar.html')

def exit(request):
    logout(request)
    return redirect('home')