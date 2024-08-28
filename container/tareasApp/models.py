from django.db import models

# Create your models here.
from django.db import models

class Mensaje(models.Model):
    contenido = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)