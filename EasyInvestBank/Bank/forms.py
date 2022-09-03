from django import forms
from .models import Transaction
from User.models import Account


class MoneyTransferForm (forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "recipients_name",
            "recipients_account_number", 
            "amount"
        ]

    def clean_amount(self): # error handling for the transaction amount
        amount = self.cleaned_data['amount'] # getting data from form
        if amount < 0:
            raise forms.ValidationError("amount can't be less than 0") # if data input is wrong return error
        return amount


    def clean_recipients_name(self): # error handling for the recipients name,
        recipients_name = self.cleaned_data['recipients_name'] # getting data from form
        try:
            Account.objects.get(full_name=recipients_name)
            return recipients_name
        except Account.DoesNotExist: # if recipient isn't in database then return error
            raise forms.ValidationError("User doesn't exist")


    def clean_recipients_account_number(self): # error handling for the recipients account number
        recipients_account_number = self.cleaned_data['recipients_account_number'] # getting data from form
        try:
            Account.objects.get(IBAN=recipients_account_number) # if recipients account number isn't in database return error
            return recipients_account_number
        except Account.DoesNotExist: # if recipients account number isn't in database return error
            raise forms.ValidationError("Account number doesn't exist")
