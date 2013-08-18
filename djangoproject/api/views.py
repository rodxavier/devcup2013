from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import User
from api.serializers import UserSerializer, OfferSerializer, DealSerializer
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

class DealOfferAPIView(generics.ListAPIView):
    model = Offer
    serializer_class = OfferSerializer
    
    def get_queryset(self):
        request = self.request
        deal_id = request.GET.get('id')
        offers = Offer.objects.filter(deal_offered_to=deal_id, is_cancelled=False, is_rejected=False)
        return offers

class UserOfferAPIView(generics.ListAPIView):
    model = Offer
    serializer_class = OfferSerializer
    
    def get_queryset(self):
        user = self.request.user
        offers = Offer.objects.filter(owner=user).order_by('-created_at')
        return offers
        
class CancelOfferAPIView(generics.ListAPIView):
    model = Offer
    serializer_class = OfferSerializer
    
    def post(self, request, *args, **kwargs):
        user = request.user
        offer_id = request.POST.get('offer_id')
        if offer_id is not None:
            offer = Offer.objects.get(id=offer_id)
            if offer.owner == user:
                offer.is_cancelled = True
                offer.save()
                return Response({'success': True}, status=status.HTTP_201_CREATED,
                                headers=headers)
        return Response({'success': False, 'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
            
class AcceptOfferAPIView(generics.ListAPIView):
    model = Offer
    serializer_class = OfferSerializer
    
    def post(self, request, *args, **kwargs):
        user = request.user
        offer_id = request.POST.get('offer_id')
        if offer_id is not None:
            offer = Offer.objects.get(id=offer_id)
            if offer.deal_offered_to.owner == user:
                offer.accept_offer()
                return Response({'success': True}, status=status.HTTP_201_CREATED,
                                headers=headers)
        return Response({'success': False, 'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
class RejectOfferAPIView(generics.ListAPIView):
    model = Offer
    serializer_class = OfferSerializer
    
    def post(self, request, *args, **kwargs):
        user = request.user
        offer_id = request.POST.get('offer_id')
        if offer_id is not None:
            offer = Offer.objects.get(id=offer_id)
            if offer.deal_offered_to.owner == user:
                offer.is_rejected = True
                return Response({'success': True}, status=status.HTTP_201_CREATED,
                                headers=headers)
        return Response({'success': False, 'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
        
class CreateDealAPIView(generics.CreateAPIView):
    serializer_class =  DealSerializer
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
            
class ListDealAPIView(generics.ListAPIView):
    model = Deal
    serializer_class = DealSerializer
    
    def get_queryset(self):
        user = self.request.user
        deals = Deal.objects.filter(is_available=True).exclude(owner=user).order_by('-created_at')
        return deals
        
class UserDealAPIView(generics.ListAPIView):
    model = Deal
    serializer_class = DealSerializer
    
    def get_queryset(self):
        user = self.request.user
        deals = Deal.objects.filter(owner=user).order_by('-created_at')
        return deals
