from django.db import models

# Create your models here.

# class Transaction(models.Model):
#     senders_name = models.CharField(max_length=100, null=True, blank=False)
#     senders_account_currency = models.CharField(max_length=100)
#     amount = models.IntegerField()
#     recipients_name = models.CharField(max_length=100)
#     recipients_account_number = models.CharField(max_length=16)
#     recipients_account_currency = models.CharField(max_length=100)
    
    
    
class Transaction_List(models.Model):
    
    sender_IBAN = models.CharField(max_length=100, default=0)
    sender_FULLNAME = models.CharField(max_length=100, default=0)
    amount = models.DecimalField(max_digits=60, decimal_places=2)
    receiver_IBAN = models.CharField(max_length=100)
    sent_at = models.DateTimeField(auto_now_add=True)