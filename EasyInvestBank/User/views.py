from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from User.forms import RegistrationForm, AccountAuthenticationForm

# Create your views here.

def registration_form(request):
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
            account = authenticate(
                email=email,
                password=raw_password,
                date_of_birth=date_of_birth,
                full_name=full_name,
                address=address,
                country=country,
            )
            login(request, account)
            return redirect("/home")
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
        return redirect("home")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                return redirect('home')
            
    else:
        form = AccountAuthenticationForm()
        
    context['login_form'] = form
    
    return render(request, 'User/login.html', context)