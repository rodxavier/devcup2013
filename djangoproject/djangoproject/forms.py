from django import forms
from marketplace.models import Deal, Offer

class CreateDealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title', 'description', 'image', 'price']

class CreateOfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ['owner', 'deal_offered_to', 'deal_owned', 'amount', 'description']
