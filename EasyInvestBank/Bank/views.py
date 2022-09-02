from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Transaction
from User.models import Account
from .forms import MoneyTransferForm
from django import forms
from django.views.generic import ListView
from django.db.models import Q



def money_transfer(request):
    if request.method == "POST":
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            # form.save()

            # making a transaction object for transaction history
            transaction = Transaction.objects.create(
                senders_name=request.user.full_name,
                recipients_name = form.cleaned_data.get("recipients_name"),
                recipients_account_number = form.cleaned_data.get("recipients_account_number"),
                amount = form.cleaned_data.get("amount"),
                )

            # Getting dest user account number
            dest_user_acc_num = transaction.recipients_account_number

            # the fields for transaction
            dest_user = Account.objects.get(IBAN=dest_user_acc_num) # FIELD 1
            transfer_amount = transaction.amount # FIELD 2
            curr_user = Account.objects.get(full_name=request.user.full_name) # FIELD 3

            # check if user balance is sufficient for transfer amount
            if curr_user.balance < transfer_amount:
                raise forms.ValidationError("Insufficient balance")
            else:
                curr_user.balance = curr_user.balance - transfer_amount
                dest_user.balance = dest_user.balance + transfer_amount

            # Save the changes before redirecting
            curr_user.save()
            dest_user.save()

        return redirect("User/home.html")
    else:
        form = MoneyTransferForm()
    return render(request, "money_transfer.html", {"form": form})


def database_transactions(request):
    transaction_data = Transaction.objects.all()

    context = {
        'transaction_data': transaction_data
    }

    return render(request, 'transactions.html', {
        'transaction_data': transaction_data
    })


class ListTransactions(ListView):
    template_name = 'transactions.html'
    model = Transaction
    context_object_name = 'transactions_data'

    def get_queryset(self): # the search function for transactions
        user = self.request.user.full_name # get logged in user full name
        transactions = Transaction.objects.filter(senders_name=user) # show only the transactions related to the user

        search = self.request.GET.get('search') # getting search data from user

        if search is not None: # if the user searched something then we're returning the
                            # search otherwise we're returning all of the transactions

            transactions = transactions.filter(
                Q(senders_name__contains=search) |
                Q(recipients_name__contains=search) |
                Q(recipients_account_number__contains=search) |
                Q(date__contains=search)
            )
        
        transactions = transactions.order_by('-date') # ordering the results by date
        return transactions
