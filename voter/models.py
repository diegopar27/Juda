from django.db import models

TYPE = (
    ('cedula', 'Cedula'),
    ('tarjeta de identidad', 'Tarjeta de identidad'),
    ('cedula extrangera', 'Cedula extrenagera'),
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
    address_of_residence = models.CharField(max_length=100,
                                            blank=False,
                                            null=False,
                                            verbose_name='Direccion de residencia')
    phone = models.CharField(max_length=100,
                             blank=False,
                             null=False,
                             verbose_name='Celular')

    def __str__(self):
        return self.name

