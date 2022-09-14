from django.test import SimpleTestCase
from django.urls import resolve, reverse
from User.views import AccountView, logout_view, registration_view


class TestUrls(SimpleTestCase):

    def test_registration_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registration_view)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_account_url_is_resolved(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func.view_class, AccountView)