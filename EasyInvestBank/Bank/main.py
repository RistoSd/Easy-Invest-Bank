from User.models import Account

def test():
    if Account.objects.filter(IBAN=123444):
        
        print('True')
    
    
    
test()