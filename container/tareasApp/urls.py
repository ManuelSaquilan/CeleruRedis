from django.urls import path
from .views import  *

app_name = "tareasApp"

urlpatterns = [
    path('mensajes/', mostrar_mensaje, name='mostrar_mensajes'),
    path('tarea/', ejecutar_tarea, name='ejecutar_tarea'),
]