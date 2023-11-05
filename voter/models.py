
from django.db import models

from commune.models import Commune
from neighborhood.models import Neighborhood
from leader.models import Leader

TYPE = (
    ('cedula de ciudadania', 'Cedula de ciudadania'),
    ('cedula extranjeria', 'Cedula extranjeria'),
)


class Voter (models.Model):
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
    name_commune = models.ForeignKey(Commune,
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE,
                                     verbose_name='Comuna')
    name_neighborhood = models.ForeignKey(Neighborhood,
                                          blank=True,
                                          null=True,
                                          on_delete=models.CASCADE,
                                          verbose_name='Barrio')
    phone = models.CharField(max_length=100,
                             blank=False,
                             null=False,
                             verbose_name='Celular')
    name_leader = models.ForeignKey(Leader,
                                    blank=True,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='Lider')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    voting_booth = models.CharField(max_length=500,
                                    blank=True,
                                    null=True,
                                    verbose_name='Puesto de votacion')

    def __str__(self):
        return self.name


