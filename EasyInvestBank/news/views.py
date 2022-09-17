import requests
from django.shortcuts import render
from pycoingecko import CoinGeckoAPI
import datetime


def home(request):
    url = (
        'https://newsapi.org/v2/top-headlines?'
        'q=Business&'
        'sortBy=popularity&'
        'apiKey=5fa0d0485aa5497d9fde386421fa8609'
    )

    response = requests.get(url).json()
    article = response['articles']

    Crypto = (
        'https://newsapi.org/v2/everything?'
        'q=Bitcoin&'
        'sortBy=popularity&'
        'apiKey=826167931ac14149bf2a52aa2d7ad964'
    )

    response1 = requests.get(Crypto).json()
    article1 = response1['articles']

    # CRYPTO PRICES >.<

    cg = CoinGeckoAPI()
    crypto_prices = cg.get_price(
        ids='bitcoin,litecoin,ethereum, dogechain, gmx, optimism,'
            ' ecash, evmos, tether, cardano, usd-coin, binancecoin,'
            ' matic-network, tron, shiba-inu',
        vs_currencies='eur',
        include_last_updated_at=True,
        include_24hr_change=True,
    )
    
    bitcoin_prices = crypto_prices.get('bitcoin')
    erhereum_prices = crypto_prices.get('ethereum')
    litecoin_prices = crypto_prices.get('litecoin')
    cardano_prices = crypto_prices.get('cardano')
    shiba_inu = crypto_prices.get('shiba-inu')
    optimism_prices = crypto_prices.get('optimism')
    ecash_prices = crypto_prices.get('ecash')
    evmos_prices = crypto_prices.get('evmos')
    tether_prices = crypto_prices.get('tether')
    usdcoin_prices = crypto_prices.get('usd-coin')
    binancecoin_prices = crypto_prices.get('binancecoin')
    maticnetwork_prices = crypto_prices.get('matic-network')
    tron_prices = crypto_prices.get('tron')
    last_updated = datetime.datetime.fromtimestamp(
        shiba_inu['last_updated_at']
        ).strftime('%c')

    trending_crypto = cg.get_search_trending()
    trending_name = []
    trending_icon = []
    trending_id = []
    for i in range(7):
        trending_name.append(trending_crypto['coins'][i]['item']['name'])
        trending_icon.append(trending_crypto['coins'][i]['item']['thumb'])
        trending_id.append(trending_crypto['coins'][i]['item']['id'])
        
    context = {
        'last_updated': last_updated,
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
        'bitcoin_prices': bitcoin_prices,
        'ethereum_prices': erhereum_prices,
        'litecoin_prices': litecoin_prices,
        'cardano_prices': cardano_prices,
        'shiba_inu': shiba_inu,
        'optimism_prices': optimism_prices,
        'ecash_prices': ecash_prices,
        'evmos_prices': evmos_prices,
        'tether_prices': tether_prices,
        'usdcoin_prices': usdcoin_prices,
        'binancecoin_prices': binancecoin_prices,
        'maticnetwork_prices': maticnetwork_prices,
        'tron_prices': tron_prices,
        'trending_name': trending_name,
        'trending_icon': trending_icon,
        'trending_id': trending_id,
    }

    return render(request, 'news/home.html', context=context)
