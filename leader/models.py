from django.db import models
from commune.models import Commune
from neighborhood.models import Neighborhood

from django.core.validators import FileExtensionValidator
import re
from django.core.exceptions import ValidationError


def validar_cadena_sin_punto(cadena):
    # Expresión regular que verifica que no haya puntos en la cadena
    patron = r'^[^.]*$'

    if not re.match(patron, cadena):
        raise ValidationError('La cadena no debe contener puntos.')


TYPE = (
    ('cedula de ciudadania', 'Cedula de ciudadania'),
    ('cedula extrangera', 'Cedula extrenagera'),
)
TYPE1 = (
    ('barrio', 'Barrio'),
    ('comuna', 'Comuna'),
)

class Leader (models.Model):
    name = models.CharField(max_length=100,
                          blank=False,
                          null=False,
                          verbose_name='Nombre')
    lastname = models.CharField(max_length=100,
                                blank=False,
                                null=False,
                                verbose_name='Apellido')
    type_of_document = models.CharField(max_length=100,
                                        blank=False,
                                        null=False,
                                        choices=TYPE,
                                        verbose_name='Tipo de documento')
    document_number = models.CharField(max_length=100,
                                       blank=False,
                                       null=False,
                                       verbose_name='Numero de documento')
    email = models.EmailField(blank=False,
                              null=False,
                              verbose_name='Correo electronico')
    address_of_residence = models.CharField(max_length=100,
                                            blank=False,
                                            null=False,
                                            verbose_name='Direccion de residencia')
    phone = models.CharField(max_length=100,
                             blank=False,
                             null=False,
                             verbose_name='Celular')
    name_commune = models.ForeignKey(Commune,
                                     blank=False,
                                     null=False,
                                     on_delete=models.CASCADE,
                                     verbose_name='Nombre de la comuna')
    name_neighborhood = models.ForeignKey(Neighborhood,
                                          blank=False,
                                          null=False,
                                          on_delete=models.CASCADE,
                                          verbose_name='Nombre del barrio')
    commune_neighborhood = models.CharField(max_length=100,
                                            blank=False,
                                            null=False,
                                            choices=TYPE1,
                                            verbose_name='comuna o barrio')

    def __str__(self):
        return self.name
