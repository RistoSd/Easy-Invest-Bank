from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from User.models import Account

from .forms import MoneyTransferForm
from .models import Transaction_List
from .utilities import currency_exchange


@login_required
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
