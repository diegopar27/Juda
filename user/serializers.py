from rest_framework.serializers import ModelSerializer

from user.models import CustomUser


class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ('password', 'groups', 'user_permissions')
        read_only_fields = ('is_staff', 'is_active', 'is_superuser')