from django.shortcuts import render
import requests
from pycoingecko import CoinGeckoAPI


def cryptoprice(request):
    cg = CoinGeckoAPI()
    crypto_prices = cg.get_price(
        ids='bitcoin,litecoin,ethereum, dogechain, gmx, optimism, ecash, evmos, tether, usd-coin, binancecoin,'
            ' matic-network, tron',
        vs_currencies='usd,eur')
    err = "000"
    currency = 'eur'  # can be 'eur' or 'usd'
    displayed_currency = currency.upper()

    bitcoin_prices = crypto_prices.get('bitcoin', {'usd': "error", 'eur': "error"})[currency]
    erhereum_prices = crypto_prices.get('ethereum', {'usd': "error", 'eur': "error"})[currency]
    litecoin_prices = crypto_prices.get('litecoin', {'usd': "error", 'eur': "error"})[currency]
    dogechain_prices = crypto_prices.get('dogechain', {'usd': "error", 'eur': "error"})[currency]
    gmx_prices = crypto_prices.get('gmx', {'usd': "error", 'eur': "error"})[currency]
    optimism_prices = crypto_prices.get('optimism', {'usd': "error", 'eur': "error"})[currency]
    ecash_prices = crypto_prices.get('ecash', {'usd': "error", 'eur': "error"})[currency]
    evmos_prices = crypto_prices.get('evmos', {'usd': "error", 'eur': "error"})[currency]
    tether_prices = crypto_prices.get('tether', {'usd': "error", 'eur': "error"})[currency]
    usdcoin_prices = crypto_prices.get('usd-coin', {'usd': "error", 'eur': "error"})[currency]
    binancecoin_prices = crypto_prices.get('binancecoin', {'usd': "error", 'eur': "error"})[currency]
    maticnetwork_prices = crypto_prices.get('matic-network', {'usd': "error", 'eur': "error"})[currency]
    tron_prices = crypto_prices.get('tron', {'usd': "error", 'eur': "error"})[currency]

    top7trending = cg.get_search_trending()
    top7names1 = top7trending['coins'][0]['item']['name']
    top7names2 = top7trending['coins'][1]['item']['name']
    top7names3 = top7trending['coins'][2]['item']['name']
    top7names4 = top7trending['coins'][3]['item']['name']
    top7names5 = top7trending['coins'][4]['item']['name']
    top7names6 = top7trending['coins'][5]['item']['name']
    top7names7 = top7trending['coins'][6]['item']['name']
    top7thumb1 = top7trending['coins'][0]['item']['thumb']
    top7thumb2 = top7trending['coins'][1]['item']['thumb']
    top7thumb3 = top7trending['coins'][2]['item']['thumb']
    top7thumb4 = top7trending['coins'][3]['item']['thumb']
    top7thumb5 = top7trending['coins'][4]['item']['thumb']
    top7thumb6 = top7trending['coins'][5]['item']['thumb']
    top7thumb7 = top7trending['coins'][6]['item']['thumb']

    context = {

        'currency': displayed_currency,

        'bitcoin_prices': bitcoin_prices,
        'ethereum_prices': erhereum_prices,
        'litecoin_prices': litecoin_prices,
        'dogechain_prices': dogechain_prices,
        'gmx_prices': gmx_prices,
        'optimism_prices': optimism_prices,
        'ecash_prices': ecash_prices,
        'evmos_prices': evmos_prices,
        'tether_prices': tether_prices,
        'usdcoin_prices': usdcoin_prices,
        'binancecoin_prices': binancecoin_prices,
        'maticnetwork_prices': maticnetwork_prices,
        'tron_prices': tron_prices,

        'top7names1': top7names1,
        'top7names2': top7names2,
        'top7names3': top7names3,
        'top7names4': top7names4,
        'top7names5': top7names5,
        'top7names6': top7names6,
        'top7names7': top7names7,
        'top7thumb1': top7thumb1,
        'top7thumb2': top7thumb2,
        'top7thumb3': top7thumb3,
        'top7thumb4': top7thumb4,
        'top7thumb5': top7thumb5,
        'top7thumb6': top7thumb6,
        'top7thumb7': top7thumb7,

    }
    return render(request, 'cryptoprice.html', context=context)
