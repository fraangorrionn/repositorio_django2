from django.shortcuts import render
from .models import Monitor
from .models import Maquina
from .models import Clase

# Create your views here.
def Monitor_list(request):
    Monitor = Monitor.objects.all()  # Obtener todos los animales
    return render(request, 'Monitor_list.html', {'Monitor': Monitor})

def Maquina_list(request):
    Maquina = Maquina.objects.all()  # Obtener todas las protectoras
    return render(request, 'Maquina_list.html', {'Maquina': Maquina})

def Clase_list(request):
    Clase = Clase.objects.all()  # Obtener todos los colaboradores
    return render(request, 'Clase_list.html', {'Clase': Clase})
