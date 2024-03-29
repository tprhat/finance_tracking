from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegistrationForm, AddDataForm, ManageBudget
from .models import Transactions


@login_required(login_url='login')
def home(request):
    transactions = Transactions.objects.filter(username=request.user)

    return render(request, 'web_backend/home.html', {"transactions": transactions})


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
    if request.method == 'POST':
        form = AddDataForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.username = request.user
            data.save()
            return redirect('home')
    else:
        form = AddDataForm()
        return render(request, 'web_backend/add_data.html', {"form": form})

@login_required(login_url='login')
def manage_budget(request):
    if request.method == 'POST':
        form = ManageBudget(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.username = request.user
            data.save()
            return redirect('home')
    else:
        form = ManageBudget()
    return render(request, 'web_backend/manage_budget.html', {"form": form})
