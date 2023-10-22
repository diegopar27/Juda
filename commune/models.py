from django.db import models

# Create your models here.


class Commune (models.Model):
    name_commune = models.CharField(max_length=100,
                                    null=False,
                                    blank=False,
                                    verbose_name='Nombre de comuna')