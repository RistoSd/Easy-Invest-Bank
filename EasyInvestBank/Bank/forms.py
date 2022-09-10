from django import forms
from .models import Transaction_List
from User.models import Account



# class MoneyTransferForm (forms.ModelForm):
#     class Meta:
#         model = Transaction
#         fields = [
#             "senders_name",
#             "recipients_name",
#             "recipients_account_number", 
#             "amount"
#         ]
        
        
        
class MoneyTransferForm(forms.ModelForm):
    

    
    amount = forms.DecimalField(max_digits=60, decimal_places=2, label='Amount')
    receiver_IBAN = forms.CharField(max_length=100)
    sender_IBAN = forms.CharField(max_length=100)
    sender_FULLNAME = forms.CharField(max_length=100)
    
    # def clean_receiver_iban(self):
    #     r_iban = self.cleaned_data['receiver_IBAN']
    #     obj = Account.objects.get(all)
    #     if r_iban not in obj.IBAN:
    #         raise forms.ValidationError("IBAN Doesnt Exist")
        # return r_iban
    
    class Meta:
        model = Transaction_List
        fields = [
            'amount',
            'receiver_IBAN',
            'sender_IBAN',
            'sender_FULLNAME'
        ]
        
        