from django import forms
from .models import Transaction_List


class MoneyTransferForm(forms.ModelForm):
    amount = forms.DecimalField(
        max_digits=60, decimal_places=2, label='Amount')
    receiver_IBAN = forms.CharField(max_length=100)
    sender_IBAN = forms.CharField(max_length=100)
    sender_FULLNAME = forms.CharField(max_length=100)

    class Meta:
        model = Transaction_List
        fields = [
            'amount',
            'receiver_IBAN',
            'sender_IBAN',
            'sender_FULLNAME'
        ]