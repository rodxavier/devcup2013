from django import forms
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.Form):
    mobile = forms.CharField(label=_("Mobile"),
        max_length=30, 
        widget=forms.TextInput(attrs={'placeholder':_('Mobile')} )
    )

    def save(self, new_user):
        new_user.mobile = self.cleaned_data.get('mobile')
        new_user.save()
        return new_user
