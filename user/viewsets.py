from rest_framework import viewsets, status

from rest_framework.response import Response

from user.models import CustomUser
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ('get', 'post', 'patch', 'delete')

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if request.data.get('password'):
                new_user = CustomUser.objects.filter(id=serializer.data['id']).first()
                new_user.set_password(request.data.get('password'))
                new_user.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)