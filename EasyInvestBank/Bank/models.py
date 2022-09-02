from django.db import models


class Transaction(models.Model):
    senders_name = models.CharField(max_length=100, null=True)
    senders_account_currency = models.CharField(max_length=100)
    amount = models.IntegerField()
    recipients_name = models.CharField(max_length=100)
    recipients_account_number = models.CharField(max_length=16)
    recipients_account_currency = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)