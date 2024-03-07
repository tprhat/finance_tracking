from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Transactions, UserBudget


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class AddDataForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ("transaction", "transaction_name")


class ManageBudget(forms.ModelForm):
    class Meta:
        model = UserBudget
        fields = ("budget",)
