from django.db import models
from commune.models import Commune
from neighborhood.models import Neighborhood

TYPE = (
    ('cedula de ciudadania', 'Cedula de ciudadania'),
    ('cedula extrangera', 'Cedula extrenagera'),
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

    def __str__(self):
        return self.name
