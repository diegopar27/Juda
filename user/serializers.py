from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user.models import CustomUser
from leader.models import Leader


class UserSerializer(serializers.ModelSerializer):

    leader = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        exclude = ('password', 'groups', 'user_permissions')
        read_only_fields = ('is_staff', 'is_active', 'is_superuser')

    @classmethod
    def get_leader(cls, leader):
        if leader:
            lider = Leader.objects.filter(email=leader.email).first()
            if lider:
                print(lider)
                return lider.id
        return None
