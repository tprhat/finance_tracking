from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'web_backend/home.html')


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url='login')
def add_data(request):
    return render(request, 'web_backend/add_data.html')