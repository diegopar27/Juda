from django.db import models
from django.core.validators import FileExtensionValidator
import re
from django.core.exceptions import ValidationError

TYPE = (
    ('cedula de ciudadania', 'Cedula de ciudadania'),
    ('cedula extrangera', 'Cedula extrenagera'),
)


def validar_cadena_sin_punto(cadena):
    # Expresión regular que verifica que no haya puntos en la cadena
    patron = r'^[^.]*$'

    if not re.match(patron, cadena):
        raise ValidationError('La cadena no debe contener puntos.')


class Candidate(models.Model):
    name = models.CharField(max_length=100,
                           blank=False,
                           null=False,
                           verbose_name='Nombre')
    last_name = models.CharField(max_length=100,
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
    phone = models.CharField(max_length=13,
                             blank=False,
                             null=False,
                             verbose_name='Celular')
    political_party = models.FileField(upload_to='imaproduct',
                             blank=True,
                             null=True,
                             verbose_name='Imagen del prodcuto',
                             validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'jpeg'])])

    Desired_position = models.CharField(max_length=50,
                                        blank=False,
                                        null=False,
                                        verbose_name='Cargo deseado')

    def __str__(self):
        return self.name
