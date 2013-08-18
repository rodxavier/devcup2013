from django import forms
from marketplace.models import Deal

class CreateDealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title', 'description', 'image', 'price']
