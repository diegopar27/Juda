from django.db import models
#from leader.models import Leader

class Neighborhood(models.Model):
    name_of_the_neighborhood = models.CharField(max_length=50,
                                                blank=False,
                                                null=False,
                                                verbose_name='Nombre del barrio')

    def __str__(self):
        return self.name_of_the_neighborhood
