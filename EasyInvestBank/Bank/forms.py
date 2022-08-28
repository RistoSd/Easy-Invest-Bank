from django import forms
from .models import Transaction


class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "recipients_name",
            "recipients_account_number", 
            "amount"
        ]