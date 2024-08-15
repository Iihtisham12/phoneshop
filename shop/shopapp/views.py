from django.shortcuts import render, redirect
from .forms import ExpenseForm, RegisterForm
from .models import Expense
from django.db.models import Sum
import datetime
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

def indexPage(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            expense_form = ExpenseForm(request.POST)
            if expense_form.is_valid():
                expense_form.save()
                return redirect('/home/')

        else:
            expense_form = ExpenseForm()
        show_date = Expense.objects.all()

        total_expenses = show_date.aggregate(Sum('amount'))
        # print(total_expenses)
        
        # yearly sum krna
        last_year = datetime.date.today() - datetime.timedelta(days=365)
        data = Expense.objects.filter(date__gt=last_year)
        yearly_sum = data.aggregate(Sum('amount'))
        # print(yearly_sum)

        # monthly sum krna
        last_month = datetime.date.today() - datetime.timedelta(days=30)
        data = Expense.objects.filter(date__gt=last_month)
        monthly_sum = data.aggregate(Sum('amount'))
        # print(monthly_sum)

        # last_week sum Krn 
        last_week = datetime.date.today() - datetime.timedelta(days=7)
        data = Expense.objects.filter(date__gt=last_week)
        weekly_sum = data.aggregate(Sum('amount'))
        # print(weekly_sum)

        deaily_sum = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
        # print(deaily_sum)

        catorical_sums = Expense.objects.filter().values('category').order_by('category').annotate(sum=Sum('amount'))
        # print(catorical_sums)
        return render(request, 'shopapp/index.html',{'expense_form':expense_form, 'show_date':show_date, 'total_expenses':total_expenses, 'yearly_data':yearly_sum, 'monthly_data':monthly_sum, 'weekly_data':weekly_sum, 'dealy_data_sum':deaily_sum, 'catorical_sums':catorical_sums})
    else:
        return redirect('/')
    

def editData(request,id):
    expense = Expense.objects.get(id=id)
    expense_form =  ExpenseForm(instance=expense)
    if request.method == "POST":
        expense = Expense.objects.get(id=id)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('/home/')

    return render(request, 'shopapp/edit.html',{'expense_form':expense_form})


def deleteData(request,id):
    if request.method == "POST" and 'delete' in request.POST:
        expense = Expense.objects.get(id=id)
        expense.delete()
    return redirect('/home/')


def singUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            singup_form = RegisterForm(request.POST)
            if singup_form.is_valid():
                singup_form.save()
                return redirect('/')
            
        else:
            singup_form = RegisterForm()
        return render(request,'shopapp/singup.html',{'form_singup':singup_form})
    else:
        return redirect('/home/')


def loGinPage(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form_login = AuthenticationForm(request=request, data=request.POST)
            if form_login.is_valid():
                uname = form_login.cleaned_data['username']
                upass = form_login.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return redirect('/home/')
        else:
            form_login = AuthenticationForm()
        return render(request, 'shopapp/login.html',{'form':form_login})
    else:
        return redirect('/home/')


def logoutMethod(request):
    logout(request)
    return redirect('/')


def change_password(request):
    if request.method == 'POST':
        pass_change = PasswordChangeForm(user=request.user, data=request.POST)
        if pass_change.is_valid():
            pass_change.save()
            update_session_auth_hash(request, pass_change.user)
            return redirect('/home/')
        
    else:
        pass_change = PasswordChangeForm(request.POST)
    return render(request,'shopapp/changepass.html',{'changepass':pass_change})