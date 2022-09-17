from Bank.views import bank_view
from django.test import SimpleTestCase
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):

    def test_bank_url_is_resolved(self):
        url = reverse('bank')
        self.assertEquals(resolve(url).func, bank_view)