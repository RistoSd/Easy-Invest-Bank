from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from User.forms import RegistrationForm, AccountAuthenticationForm
import requests
import json


# Create your views here.

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
        return redirect("/login")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                return redirect('/home')
            
    else:
        form = AccountAuthenticationForm()
        
    context['login_form'] = form
    
    return render(request, 'User/login.html', context)




def logout_view(request):
    logout(request)
    return redirect('/home')


def home(request):
    url1 = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=business&'
           'pagesize=1&'
           'q=crypto&'
           'apiKey=826167931ac14149bf2a52aa2d7ad964')
    response = requests.get(url1).json()
    url = str(response['articles'][0]['url'])
    title = str(response['articles'][0]['title'])
    image_url = str(response['articles'][0]['urlToImage'])
    url2 = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=business&'
           'pagesize=1&'
           #'q=cryptocurrencies&'
           'apiKey=826167931ac14149bf2a52aa2d7ad964')
    response2 = requests.get(url2).json()
    url2 = str(response2['articles'][0]['url'])
    title2 = str(response2['articles'][0]['title'])
    image_url2 = str(response2['articles'][0]['urlToImage'])
    
    url3 = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=business&'
           'pagesize=1&'
           #'q=cryptocurrencies&'
           'apiKey=826167931ac14149bf2a52aa2d7ad964')
    response3 = requests.get(url3).json()
    url3 = str(response3['articles'][0]['url'])
    title3 = str(response3['articles'][0]['title'])
    image_url3 = str(response3['articles'][0]['urlToImage'])



    context = {
        'url': url,
        'title': title,
        'image': image_url,
        'url2': url2,
        'title2': title2,
        'image2': image_url2,
        'url3': url3,
        'title3': title3,
        'image3': image_url3,
    }
    return render(request, 'User/home.html', context=context)