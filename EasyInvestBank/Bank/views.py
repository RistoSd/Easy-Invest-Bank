from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Transaction
from User.models import Account
from .forms import MoneyTransferForm
from django import forms
from django.views.generic import ListView


def money_transfer(request):
    if request.method == "POST":
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            # form.save()

            transaction = Transaction.objects.create(
                senders_name=request.user.full_name,
                recipients_name = form.cleaned_data.get("recipients_name"),
                recipients_account_number = form.cleaned_data.get("recipients_account_number"),
                amount = form.cleaned_data.get("amount")
                )

            dest_user_acc_num = transaction.recipients_account_number

            dest_user = Account.objects.get(IBAN=dest_user_acc_num) # FIELD 1
            transfer_amount = transaction.amount # FIELD 2
            curr_user = Account.objects.get(full_name=request.user.full_name) # FIELD 3

            # Now transfer the money!
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
