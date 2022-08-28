"""EasyInvestBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import path, re_path
from Bank.views import money_transfer
from news.views import news
from User.views import registration_view, login_form, home, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', news),
    re_path(r"^money_transfer/", money_transfer, name = "money_transfer"),
    path('register/', registration_view, name='register'),
    path('login/', login_form, name='login'),
    path('home/', home),
    path('logout/', logout_view, name='logout'),

]
