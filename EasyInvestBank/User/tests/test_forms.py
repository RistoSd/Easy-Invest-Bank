from django.test import TestCase
from User.forms import RegistrationForm


class TestForms(TestCase):

    def test_registration_form_valid_data(self):
        form = RegistrationForm(
            data={
                'email': 'test@gmail.com',
                'date_of_birth': '2022-10-12',
                'full_name': 'Test User',
                'address': 'test st 54',
                'country': 'EE',
                'password1': 'P2ssw0rD5467',
                'password2': 'P2ssw0rD5467',
                'currency': 'EUR',
            }
        )

        self.assertTrue(form.is_valid())


    def test_registration_form_no_data(self):
        form = RegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)