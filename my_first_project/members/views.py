from django.shortcuts import render

# Create your views here.

def members(request):
    contexto ={
        'curso': 'Django para Principiantes',
        'duracion': 40,
        'nivel': 'Básico'
    }
    return render(request, 'miprimer.html', contexto)

def datos_estudiante(request):
    nombre_completo={
        'nombre': 'Daniel Uribe',
        'puntuacion': 90,
        'fecha_inscripcion': '01/02/2026'
    }
    return render(request, 'miprimer.html', nombre_completo)

def tienda(request):
    productos = [
        {'nombre': 'Laptop', 'precio': 1200, 'disponible': True},
        {'nombre': 'Mouse', 'precio': 25, 'disponible': True},
        {'nombre': 'Teclado', 'precio': 45, 'disponible': False},
        {'nombre': 'Monitor', 'precio': 300, 'disponible': True},
        {'nombre': 'Tablet', 'precio': 350, 'disponible': False}
    ]
    contexto = {
        'nombre_tienda': 'Inventario de la Tienda',
        'sub1': 'Total de Productos: ',
        'productos': productos
    }
    return render(request, 'miprimer.html', contexto)
