from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from annoying.functions import get_object_or_None
from django.db.models import Q
from .models import AugustUser, Referral
from .forms import SignupForm
from django import forms
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'signup/index.html')

def sign_up(request):
    users = AugustUser.objects.all()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            #Get form data
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            referral_code_used = form.cleaned_data.get('referral_code_used')

            #Check if user already exists
            user = AugustUser.objects.filter(Q(phone=phone) | Q(email=email))
            print("form is valid")
            if user:
                print("user already exists");
                # raise forms.ValidationError('User already exists')
            else:
                print("User not found, Create user");
                #Create user
                form.save()
                return render(request, 'signup/thankyou.html')
        else:
            err=form.errors
            ctx = {'err':err}
            return render(request, 'signup/thankyou.html', ctx)
            
    else:
        form = SignupForm() 
        print(form.errors);  

    context = {'form': form}
    return render(request, 'signup/signup.html', context)


def thankyou(request):

    return render(request, 'signup/thankyou.html')
