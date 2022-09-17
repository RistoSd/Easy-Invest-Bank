from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from User.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'exampleInputEmail1',
            'style': 'max-width: 300px',
        }
        )
    )

    class Meta:
        model = Account
        fields = ('email', 'date_of_birth', 'full_name', 'address',
                  'country', 'password1', 'password2', 'currency')


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Wrong email or password!')


class PersonalInformationForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['full_name', 'address',]
        exclude = ('date_of_birth', 'currency', 'country',)
        
        
class EmailUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=255, widget=(forms.EmailInput(attrs={
        'class': 'form-control',
    })))
    
    class Meta:
        model = Account
        fields = ['email',]
   

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = Account