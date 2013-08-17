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
    class Meta:
        model = Offer
        fields = ('id', 'owner', 'deal_offered_to', 'deal_owned', 'amount', 'description',
                    'is_accepted', 'is_cancelled', 'created_at', 'updated_at')
                    
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
