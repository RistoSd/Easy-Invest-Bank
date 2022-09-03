from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from User.models import Transaction_List1

from User.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=255, help_text='Required. Enter a valid email address')
    
    class Meta:
        model = Account
        fields = ('email', 'date_of_birth', 'full_name', 'address', 'country', 'password1', 'password2')
        
        
class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Account
        fields = ('email', 'password')    
        
        
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Invalid login')
        
        
        
# Risto's Payment System Remade

class MoneyTransferForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=20, decimal_places=2, label='Amount')
    receiver_IBAN = forms.CharField(max_length=100)
    
    class Meta:
        model = Transaction_List1
        fields = [
            'amount',
            'receiver_IBAN',
        ]

        
        