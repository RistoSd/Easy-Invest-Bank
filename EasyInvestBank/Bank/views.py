from unicodedata import decimal
from xml.dom import ValidationErr
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Transaction_List
from User.models import Account
from .forms import MoneyTransferForm
from django import forms
from django.contrib import messages
import requests
from decimal import Decimal

# Create your views here.
def currency_exchange(sender_curr, reciever_curr, amount):
    url = 'https://exchange-rates.abstractapi.com/v1/convert'
    querystring = {'api_key': 'c6982eecf09f4920af0a2b426ed3d252', 'base':sender_curr, 'target': reciever_curr, 'base_amount': amount}
    response = requests.get(url, params=querystring).json()
    converted_amount = response.get('converted_amount')
    return round(converted_amount, 2)




def bank_view(request):   
    queryset = Transaction_List.objects.all()
    ctx = {}
    
    if request.method == 'POST':     
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
           
            sender_IBAN = Account.objects.get(IBAN=request.user.IBAN) # IBAN
            
            try:
                
                receiver_IBAN_FORM = form.cleaned_data['receiver_IBAN']
                receiver_IBAN = Account.objects.get(IBAN=receiver_IBAN_FORM)
            except Account.DoesNotExist:
                receiver_IBAN = None

            if receiver_IBAN:
                messages.success(request, 'Money Sent Successfully!')
                amount = form.cleaned_data['amount']
                
                #Risto Currency Exchange ->
                exchanged_currency = currency_exchange(
                sender_IBAN.currency, receiver_IBAN.currency, amount)
                
                sender_IBAN.balance = sender_IBAN.balance - amount
                print(exchanged_currency)
                receiver_IBAN.balance = receiver_IBAN.balance + Decimal(exchanged_currency)
                
                sender_IBAN.save()
                receiver_IBAN.save()
                return redirect('/bank/')
                
            else:
                Transaction_List.objects.filter(receiver_IBAN=receiver_IBAN_FORM).delete()
                messages.error(request, 'IBAN Number Doesnt Exist!')
            
        else:
            form = MoneyTransferForm()
    ctx = {'transaction_list': queryset}
    return render(request, 'Bank/bank.html', ctx)






















# RISTO PAYMENT TRANSACTION SYSTEM

# def money_transfer(request):
#     if request.method == "POST":
#         form = MoneyTransferForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             temp_user_username = form.cleaned_data.get("recipients_name")
#             temp_user = Transaction.objects.filter(senders_name=temp_user_username)
#             # dest_user_acc_num = form["recipients_account_number"].value()
#             dest_user_acc_num = form.cleaned_data.get("recipients_account_number")
#             temp = temp_user # NOTE: Delete this instance once money transfer is done
            
#             dest_user = Account.objects.get(IBAN=dest_user_acc_num) # FIELD 1
#             transfer_amount = int(form.cleaned_data.get("amount"))
#             # transfer_amount = int(form["amount"].value()) # FIELD 2
#             curr_user = Account.objects.get(full_name=request.user.full_name) # FIELD 3
#             if curr_user.balance < transfer_amount:
#                 raise forms.ValidationError('Account balance too small')
#             # Now transfer the money!
#             curr_user.balance = curr_user.balance - transfer_amount
#             dest_user.balance = dest_user.balance + transfer_amount

#             # Save the changes before redirecting
#             curr_user.save()
#             dest_user.save()

#             temp.delete() # NOTE: Now deleting the instance for future money transactions

#         # return redirect("news.html")
#     else:
#         form = MoneyTransferForm()
#     return render(request, "money_transfer.html", {"form": form})