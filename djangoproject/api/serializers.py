from rest_framework import serializers

from accounts.models import User
from marketplace.models import Deal, Offer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'mobile')
        
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.username = attrs.get('username', instance.username)
            instance.email = attrs.get('email', instance.email)
            instance.mobile = attrs.get('mobile', instance.mobile)
            return instance
        return User(**attrs)
        
class OfferSerializer(serializers.ModelSerializer):
    owner_username = serializers.SerializerMethodField('get_owner_username')
    owner_email = serializers.SerializerMethodField('get_owner_email')
    owner_mobile = serializers.SerializerMethodField('get_owner_mobile')

    class Meta:
        model = Offer
        fields = ('id', 'owner', 'deal_offered_to', 'deal_owned', 'amount', 'description',
                    'is_accepted', 'is_cancelled', 'created_at', 'updated_at',
                    'owner_username', 'owner_email', 'owner_mobile')
                    
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.owner = attrs.get('owner', instance.owner)
            instance.deal_offered_to = attrs.get('deal_offerred_to', instance.deal_offered_to)
            instance.deal_owned = attrs.get('deal_owned', instance.deal_owned)
            instance.amount = attrs.get('amount', instance.amount)
            instance.description = attrs.get('description', instance.description)
            instance.is_accepted = attrs.get('is_accepted', instance.is_accepted)
            instance.is_cancelled = attrs.get('is_cancelled', instance.is_cancelled)
        return Offer(**attrs)
        
    def get_owner_username(self, obj):
        return obj.owner.username
        
    def get_owner_email(self, obj):
        return obj.owner.email
        
    def get_owner_mobile(self, obj):
        return obj.owner.mobile
        
class DealSerializer(serializers.ModelSerializer):
    owner_username = serializers.SerializerMethodField('get_owner_username')
    owner_email = serializers.SerializerMethodField('get_owner_email')
    owner_mobile = serializers.SerializerMethodField('get_owner_mobile')
    image_url = serializers.SerializerMethodField('get_image_url')
 
    class Meta:
        model = Deal
        fields = ('id', 'owner', 'title', 'description', 'price', 'image', 'owner_username',
                    'owner_email', 'owner_mobile', 'image_url', 'is_available', 'is_sold', 'is_open')
        
    def restore_object(self, attrs, instance=None):
        if instance:
            instance.owner = attrs.get('owner', instance.owner)
            instance.title = attrs.get('title', instance.title)
            instance.price = attrs.get('price', instance.price)
            instance.description = attrs.get('description', instance.description)
            instance.is_available = attrs.get('is_available', instance.is_available)
            instance.is_sold = attrs.get('is_sold', instance.is_sold)
            instance.is_open = attrs.get('is_open', instance.is_open)
        return Deal(**attrs)
        
    def get_image_url(self, obj):
        return obj.image.url
        
    def get_owner_username(self, obj):
        return obj.owner.username
        
    def get_owner_email(self, obj):
        return obj.owner.email
        
    def get_owner_mobile(self, obj):
        return obj.owner.mobile
