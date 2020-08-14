from django.shortcuts import render
from django.utils import timezone
from .models import AugustUser
from .forms import SignupForm

# Create your views here.

def sign_up(request):
    users = AugustUser.objects.all()

    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'signup/signup.html', context)
