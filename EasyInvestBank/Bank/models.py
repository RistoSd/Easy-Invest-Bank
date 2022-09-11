from django.db import models


class Transaction_List(models.Model):

    sender_IBAN = models.CharField(max_length=100, default=0)
    sender_FULLNAME = models.CharField(max_length=100, default=0)
    amount = models.DecimalField(max_digits=60, decimal_places=2)
    receiver_IBAN = models.CharField(max_length=100)
    sent_at = models.DateTimeField(auto_now_add=True)
