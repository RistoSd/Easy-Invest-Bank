from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
crypto_prices = cg.get_price(
    ids='bitcoin, litecoin',
    vs_currencies='eur',
    include_last_updated_at=True,
    include_24hr_change=True,
    )

print(crypto_prices.get('bitcoin'))