from Bank.views import bank_view
from django.contrib import admin
from django.urls import path
from Bank.views import bank_view
from User.views import registration_view, login_form, logout_view, account_view
from news.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name='register'),
    path('login/', login_form, name='login'),
    path('', home, name='home'),
    path('logout/', logout_view, name='logout'),
    path('bank/', bank_view, name='bank'),
    path('account/', account_view, name='account'),
]
