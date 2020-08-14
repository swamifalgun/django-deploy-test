from django import forms

from .models import AugustUser, Referral

class SignupForm(forms.ModelForm): 

    class Meta:
        model = AugustUser
        fields = ('first_name', 'last_name', 'email', 'phone')