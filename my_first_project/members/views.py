from django.shortcuts import render

# Create your views here.

def members(request):
    contexto ={
        'curso': 'Django para Principiantes',
        'duracion': 40,
        'nivel': 'Básico'
    }
    return render(request, 'miprimer.html', contexto)