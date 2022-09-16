from Bank.models import Transaction_List
from django.test import TestCase


class TestModels(TestCase):
    
    def setUp(self):
        self.transaction = Transaction_List.objects.create(
            sender_IBAN = 722282588260, 
            sender_FULLNAME = 'Tester',
            amount = 10,
            receiver_IBAN = 722282588261,
        )

    def test_object_creation(self):
        self.assertEquals(self.transaction.sender_IBAN, 722282588260)