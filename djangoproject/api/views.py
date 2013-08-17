from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import User
from api.serializers import UserSerializer, OfferSerializer
from marketplace.models import Deal, Offer

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
            
class CreateOfferAPIView(generics.CreateAPIView):
    serializer_class = OfferSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        data = request.DATA.copy()
        data['owner'] = request.user.id
        serializer = self.get_serializer(data=data, files=request.FILES)
        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save(force_insert=True)
            self.post_save(self.object, created=True)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,
                            headers=headers)
        else:
            return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)
