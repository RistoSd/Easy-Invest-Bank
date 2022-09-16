from django.test import TestCase
from User.models import Account


class TestModels(TestCase):
    
    def setUp(self):
        self.account = Account.objects.create(
            email = 'test@gmail.com',
            date_of_birth = '2022-10-12',
            full_name = 'Test User',
            address = 'test st 54',
            country = 'EE',
        )

    def test_object_creation(self):
        self.assertEquals(self.account.email, 'test@gmail.com')

    def test_object_balance(self):
        self.assertEquals(self.account.balance, 0)

    def test_object_currency(self):
        self.assertEquals(self.account.currency, 'EUR')