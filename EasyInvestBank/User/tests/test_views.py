from django.test import TestCase, Client
from django.urls import reverse
import requests


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.account_url = reverse('account')

    def test_registration_get(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'User/register.html')


    def test_registration_post(self):
        response = self.client.post(
            self.register_url, {
                'email': 'test@gmail.com',
                'raw_password': 'P2ssw0rD5467',
                'date_of_birth': '2022-10-12',
                'full_name': 'Test User',
                'address': 'test st 54',
                'country': 'EE',
                'currency': 'EUR', 
            }
        )
        self.assertEquals(response.status_code, 200)
    

    def test_registration_post_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEquals(response.status_code, 200)


    def test_login_get(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)


    def test_login_post(self):
        response = self.client.post(
            self.login_url, {
                'email': 'test@gmail.com',
                'password': 'P2ssw0rD5467',
            }
        )
        self.assertEquals(response.status_code, 200)
    

    def test_login_post_no_data(self):
        response = self.client.post(self.login_url)
        self.assertEquals(response.status_code, 200)

    
    def test_logout_get(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)

    
    def test_account_get(self):
        response = self.client.get(self.account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'User/account.html')


    def test_account_post(self):
        response = self.client.post(
            self.account_url, {
                'old_password': 'P2ssw0rD5467',
                'new_password1': 'P2ssw0rD5468',
                'new_password2': 'P2ssw0rD5468'
            }
        )
        self.assertEquals(response.status_code, 200)
    

    def test_account_post_no_data(self):
        response = self.client.post(self.account_url)
        self.assertEquals(response.status_code, 200)
