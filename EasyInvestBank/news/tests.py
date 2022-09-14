from django.test import TestCase
import requests


class TestAPi(TestCase):

    def test_pycoingecko_api_get_price(self):
        response = requests.get(
            'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
        )
        self.assertEquals(response.status_code, 200)

    def test_pycoingecko_api_get_search_trending(self):
        response = requests.get(
            'https://api.coingecko.com/api/v3/search/trending'
        )
        self.assertEquals(response.status_code, 200)