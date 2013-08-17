from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from accounts.models import User
from api.serializers import UserSerializer

class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serialized = UserSerializer(data=request.DATA)
        if serialized.is_valid():
            user = User.objects.create_user(
                serialized.init_data['username'],
                serialized.init_data['email'],
                serialized.init_data['password'],
                mobile=serialized.init_data['mobile']
            )
            token = Token.objects.get_or_create(user=user)[0]
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)