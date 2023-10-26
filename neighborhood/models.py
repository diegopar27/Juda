from django.db import models
#from leader.models import Leader
from commune.models import Commune


class Neighborhood(models.Model):
    name_of_the_neighborhood = models.CharField(max_length=50,
                                                blank=False,
                                                null=False,
                                                verbose_name='Nombre del barrio')
    n_commune = models.ForeignKey(Commune,
                                  blank=True,
                                  null=True,
                                  on_delete=models.CASCADE,
                                  verbose_name='nombre de la comuna')

    def __str__(self):
        return self.name_of_the_neighborhood
