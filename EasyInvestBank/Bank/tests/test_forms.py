from django.test import SimpleTestCase
from Bank.forms import MoneyTransferForm


class TestViews(SimpleTestCase):

    def test_transfer_form_valid_data(self):
        form = MoneyTransferForm(
            data={
                'amount': 10,
                'receiver_IBAN': 722282588260,
                'sender_IBAN': 646367277900,
                'sender_FULLNAME': 'Jason'
            }
        )

        self.assertTrue(form.is_valid())

    def test_transfer_form_no_data(self):
        form = MoneyTransferForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
