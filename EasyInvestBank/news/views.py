from django.shortcuts import render
import requests
from pycoingecko import CoinGeckoAPI


def home(request):
    # NEWS
    url = ('https://newsapi.org/v2/everything?'
        'q=Business&'
        'sortBy=popularity&'
        'apiKey=5fa0d0485aa5497d9fde386421fa8609')

    response = requests.get(url).json()
    article = response['articles']
         
    Crypto = ('https://newsapi.org/v2/everything?'
        'q=Bitcoin&'
        'sortBy=popularity&'
        'apiKey=826167931ac14149bf2a52aa2d7ad964')

    response1 = requests.get(Crypto).json()
    article1 = response1['articles']
    
    
    # CRYPTO PRICES >.<
    
    cg = CoinGeckoAPI()
    crypto_prices = cg.get_price(
        ids='bitcoin,litecoin,ethereum, dogechain, gmx, optimism, ecash, evmos, tether, usd-coin, binancecoin,'
            ' matic-network, tron',
        vs_currencies='usd,eur')

    currency = 'eur'  # can be 'eur' or 'usd'
    displayed_currency = currency.upper()

    bitcoin_prices = crypto_prices['bitcoin'][currency]
    erhereum_prices = crypto_prices['ethereum'][currency]
    litecoin_prices = crypto_prices['litecoin'][currency]
    dogechain_prices = crypto_prices['dogechain'][currency]
    gmx_prices = crypto_prices['gmx'][currency]
    optimism_prices = crypto_prices['optimism'][currency]
    ecash_prices = crypto_prices['ecash'][currency]
    evmos_prices = crypto_prices['evmos'][currency]
    tether_prices = crypto_prices['tether'][currency]
    usdcoin_prices = crypto_prices['usd-coin'][currency]
    binancecoin_prices = crypto_prices['binancecoin'][currency]
    maticnetwork_prices = crypto_prices['matic-network'][currency]
    tron_prices = crypto_prices['tron'][currency]

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
        'url': article[0]['url'],
        'title': article[0]['title'],
        'image': article[0]['urlToImage'],
        'url1': article[1]['url'],
        'title1': article[1]['title'],
        'image1': article[1]['urlToImage'],
        'url2': article[2]['url'],
        'title2': article[2]['title'],
        'image2': article[2]['urlToImage'],
        'url5': article1[0]['url'],
        'title5': article1[0]['title'],
        'image5': article1[0]['urlToImage'],
        'url6': article1[1]['url'],
        'title6': article1[1]['title'],
        'image6': article1[1]['urlToImage'],
        'url7': article1[2]['url'],
        'title7': article1[2]['title'],
        'image7': article1[2]['urlToImage'],
        
        # Crypto stuff >.<
        
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
    return render(request, 'news/home.html', context=context)




