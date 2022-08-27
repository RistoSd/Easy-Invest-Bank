from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Transaction
from User.models import Account
from . import forms
from . import models

# Create your views here.

def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
            
            temp_user = models.Transaction.objects.filter(senders_name=request.user.username)
            dest_user_acc_num = form["recipients_account_number"].value()

            temp = temp_user # NOTE: Delete this instance once money transfer is done
            
            dest_user = models.Account.objects.get(IBAN=dest_user_acc_num) # FIELD 1
            transfer_amount = int(form["amount"].value()) # FIELD 2
            curr_user = models.Account.objects.get(user=request.user) # FIELD 3

            # Now transfer the money!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

            # Save the changes before redirecting
            curr_user.save()
            dest_user.save()

            temp.delete() # NOTE: Now deleting the instance for future money transactions

        return redirect("users.html")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "money_transfer.html", {"form": form})