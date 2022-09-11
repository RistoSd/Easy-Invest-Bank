from django.shortcuts import render, redirect
from .models import Transaction_List
from User.models import Account
from .forms import MoneyTransferForm
from django.contrib import messages
import requests
from decimal import Decimal


def currency_exchange(sender_curr, reciever_curr, amount):
    url = 'https://exchange-rates.abstractapi.com/v1/convert'
    querystring = {
        'api_key': 'c6982eecf09f4920af0a2b426ed3d252',
        'base': sender_curr,
        'target': reciever_curr,
        'base_amount': amount
    }
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

            sender_IBAN = Account.objects.get(IBAN=request.user.IBAN)

            try:
                receiver_IBAN_FORM = form.cleaned_data['receiver_IBAN']
                receiver_IBAN = Account.objects.get(IBAN=receiver_IBAN_FORM)
            except Account.DoesNotExist:
                receiver_IBAN = None

            if receiver_IBAN:
                messages.success(request, 'Money Sent Successfully!')
                amount = form.cleaned_data['amount']

                exchanged_currency = currency_exchange(
                    sender_IBAN.currency, receiver_IBAN.currency, amount)

                sender_IBAN.balance = sender_IBAN.balance - amount
                print(exchanged_currency)
                receiver_IBAN.balance = receiver_IBAN.balance + \
                    Decimal(exchanged_currency)

                sender_IBAN.save()
                receiver_IBAN.save()
                return redirect('/bank/')
            else:
                Transaction_List.objects.filter(
                    receiver_IBAN=receiver_IBAN_FORM).delete()
                messages.error(request, 'IBAN Number Doesnt Exist!')

        else:
            form = MoneyTransferForm()
    ctx = {'transaction_list': queryset}
    return render(request, 'Bank/bank.html', ctx)
