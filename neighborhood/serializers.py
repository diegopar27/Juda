from rest_framework.serializers import ModelSerializer
from neighborhood.models import Neighborhood
from commune.models import Commune
from rest_framework import serializers


class NeighborhoodSerializer(ModelSerializer):
    commune = serializers.CharField(source='n_commune.name_commune')

    class Meta:
        model = Neighborhood
        fields = ['id', 'name_of_the_neighborhood', 'n_commune','commune',
                    ]

        def get_commune(self, obj):
            # Define cómo obtener el valor del campo 'commune'
            try:
                comuna = Commune.objects.get(comuna_number=obj.n_commune)
                return comuna.name_commune
            except Commune.DoesNotExist:
                return None