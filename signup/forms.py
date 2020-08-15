from django import forms

from .models import AugustUser, Referral

class SignupForm(forms.ModelForm): 

    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=10, required=True)
    referral_code_used = forms.CharField(max_length=11, required=False)
    

    class Meta:
        model = AugustUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'referral_code_used')