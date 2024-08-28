from celery import shared_task
from datetime import datetime
from .models import Mensaje



@shared_task
def escribir_hola_mundo():
    try:
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mensaje = f"Hola Mundo - Ejecutado a las {tiempo}"
        nuevo_mensaje = Mensaje.objects.create(contenido=mensaje)
        print(f"Mensaje creado con ID: {nuevo_mensaje.id}")
        return mensaje
    except Exception as e:
        print(f"Error al crear mensaje: {str(e)}")
        import traceback
        print(traceback.format_exc())
        raise

