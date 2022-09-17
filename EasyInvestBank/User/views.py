from .models import Account
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from User.forms import (
    RegistrationForm, 
    AccountAuthenticationForm, 
    PasswordChangeForm,
    EmailUpdateForm,
    PersonalInformationForm,
)
from django.contrib import messages



def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            full_name = form.cleaned_data.get('full_name')
            address = form.cleaned_data.get('address')
            country = form.cleaned_data.get('country')
            currency = form.cleaned_data.get('currency')
            account = authenticate(
                email=email,
                password=raw_password,
                date_of_birth=date_of_birth,
                full_name=full_name,
                address=address,
                country=country,
                currency=currency,
            )
            login(request, account)
            return redirect("/")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'User/register.html', context)


def login_form(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("/login")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('/')

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, 'User/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def account_view(request):
    personal_form = PersonalInformationForm
    email_form = EmailUpdateForm
    password_form = PasswordChangeForm(request.user)
    
    if request.POST:
        if 'email_form' in request.POST:
            email_form = EmailUpdateForm(request.POST, instance=request.user)
            if email_form.is_valid():
                email_check = email_form.cleaned_data.get('email')
                email_list = Account.objects.filter(
                    email=email_check
                    ).exists()
                
                if not email_list:
                    email_form.save()
                    messages.success(request, 'Email updated!')
                else:
                    messages.error(request, 'Email is already taken!')
                
        if 'personal_form' in request.POST:
            personal_form = PersonalInformationForm(
                request.POST, 
                instance=request.user
            )
            if personal_form.is_valid():
                messages.success(request, 'Personal information updated!')
                personal_form.save()
                
        if 'password_form' in request.POST:
            password_form = PasswordChangeForm(
                request.user,
                request.POST,
            )
            if password_form.is_valid():
                messages.success(request, 'Password changed successfully!')
                password_form.save()

    ctx = {
        'email_form': email_form,
        'personal_form': personal_form,
        'password_form': password_form,
    }
    
    return render(request, 'User/account.html', ctx)

            