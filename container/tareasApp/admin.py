from django.contrib import admin
from .models import Mensaje
from .tasks import escribir_hola_mundo

admin.site.register(Mensaje)