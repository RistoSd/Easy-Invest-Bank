from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate
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
            raise forms.ValidationError('Invalid login')


class AccountPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = Account
        fields = ('old_password', 'new_password1', 'new_password2')

        Widgets = {
            'old_password': forms.PasswordInput(
                attrs={'class': 'form-control'}
            ),
            'new_password1': forms.PasswordInput(
                attrs={'class': 'form-control'}
            ),
            'new_password2': forms.PasswordInput(
                attrs={'class': 'form-control'}
            )
        }
