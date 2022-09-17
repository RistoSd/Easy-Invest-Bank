import requests
from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.bank_url = reverse('bank')


    def test_transaction_get(self):
        response = self.client.get(self.bank_url)
        self.assertEquals(response.status_code, 302)


    def test_transaction_post(self):
        response = self.client.post(
            self.bank_url, {
            'receiver_IBAN': 722282588260,
            'amount': 20,
            }
        )
        self.assertEquals(response.status_code, 302)

    
    def test_transaction_post_no_data(self):
        response = self.client.post(self.bank_url)
        self.assertEquals(response.status_code, 302)


    def test_currency_exchange_get(self):
        url = 'https://exchange-rates.abstractapi.com/v1/convert'
        querystring = {
            'api_key': 'c6982eecf09f4920af0a2b426ed3d252', 
            'base':'EUR', 
            'target': 'USD', 
            'base_amount': 10
            }
        response = requests.get(url, params=querystring)
        self.assertEquals(response.status_code, 200)