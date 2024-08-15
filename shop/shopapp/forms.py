from django.forms import ModelForm
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense

        fields = [ 'name', 'amount', 'category']


class RegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Password (again)',widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

        labels = {'username':'UserName','first_name':'F/Name','last_name':'L/Name','email':'Email'}