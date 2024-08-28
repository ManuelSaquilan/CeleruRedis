from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Mensaje
from django.http import HttpResponse
from .tasks import escribir_hola_mundo

def mostrar_mensaje(request):
    ultimo_mensaje = Mensaje.objects.last()
    return render(request, 'mostrar_mensaje.html', {'mensaje': ultimo_mensaje})


def ejecutar_tarea(request):
    try:
        resultado = escribir_hola_mundo()
        return HttpResponse(f"Tarea ejecutada: {resultado}")
    except Exception as e:
        return HttpResponse(f"Error al ejecutar la tarea: {str(e)}")