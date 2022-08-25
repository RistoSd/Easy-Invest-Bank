from django.db import models

# Create your models here.

class Transaction(models.Model):
    senders_name = models.CharField(max_length=100, null=True, blank=False)
    senders_account_currency = models.CharField(max_length=100)
    amount = models.IntegerField()
    recipients_name = models.CharField(max_length=100)
    recipients_account_number = models.IntegerField()
    recipients_account_currency = models.CharField(max_length=100)