from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Transaction_List
from User.models import Account
from .forms import MoneyTransferForm
from django import forms


# Create your views here.

def bank_view(request):   
    queryset = Transaction_List.objects.all()
    context = {}
    
    if request.method == 'POST':
        
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            SENDER_IBAN = Account.objects.get(IBAN=request.user.IBAN) # IBAN
            
            RECEIVER_IBAN_FORM = form.cleaned_data['receiver_IBAN']
            RECEIVER_IBAN = Account.objects.get(IBAN=RECEIVER_IBAN_FORM)
            
            AMOUNT = form.cleaned_data['amount']
            if SENDER_IBAN.balance < AMOUNT:
                pass # Made with html that you cant surpass user.balance, might use as secondhand proofing
            
            SENDER_IBAN.balance = SENDER_IBAN.balance - AMOUNT
            
            RECEIVER_IBAN.balance = RECEIVER_IBAN.balance + AMOUNT
            
            SENDER_IBAN.save()
            RECEIVER_IBAN.save()
            return redirect('/bank/')
            
    else:
        form = MoneyTransferForm()
    context= {'transaction_list': queryset}
    return render(request, 'Bank/bank.html', context)






















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