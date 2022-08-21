from django.shortcuts import render
import requests

def news(request):
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=business&'
           'pagesize=1&'
           #'q=cryptocurrencies&'
           'apiKey=826167931ac14149bf2a52aa2d7ad964')
    response = requests.get(url).json()

    context = {
        'news': response
    }
    return render(request, 'news.html', context=context)

