from django.db import models
from leader.models import Leader

class Neighborhood(models.Model):
    name_of_the_neighborhood = models.CharField(max_length=50,
                                                blank=False,
                                                null=False,
                                                verbose_name='Nombre del barrio')

    def __str__(self):
        return self.name_of_the_neighborhood


class Neighborhood_leader(models.Model):
    neighborhoods = models.ForeignKey(Neighborhood,
                                      blank=True,
                                      null=True,
                                      on_delete=models.CASCADE,
                                      verbose_name='user')
    leaders = models.ForeignKey(Leader,
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='Lider')
