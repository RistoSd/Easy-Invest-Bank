from Bank.views import bank_view
from django.contrib import admin
from django.urls import path
from news.views import home
from User.views import AccountView, login_form, logout_view, registration_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name='register'),
    path('login/', login_form, name='login'),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('bank/', bank_view, name='bank'),
    path('account/', AccountView.as_view(), name='account')
]
