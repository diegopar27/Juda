from django.db import models
from django.core.validators import FileExtensionValidator
import re
from django.core.exceptions import ValidationError

# Create your models here.

def validar_cadena_sin_punto(cadena):
    # Expresión regular que verifica que no haya puntos en la cadena
    patron = r'^[^.]*$'

    if not re.match(patron, cadena):
        raise ValidationError('La cadena no debe contener puntos.')

class Commune (models.Model):
    name_commune = models.CharField(max_length=100,
                                    null=False,
                                    blank=False,
                                    verbose_name='Nombre de comuna')