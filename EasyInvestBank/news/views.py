from django.shortcuts import render
import requests
import json


def news(request):
    url1 = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=business&'
           'pagesize=1&'
           'q=crypto&'
           'apiKey=826167931ac14149bf2a52aa2d7ad964')
    response = requests.get(url1).json()
    url = str(response['articles'][0]['url'])
    title = str(response['articles'][0]['title'])
    image_url = str(response['articles'][0]['urlToImage'])
    url2 = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'category=business&'
           'pagesize=1&'
           #'q=cryptocurrencies&'
           'apiKey=826167931ac14149bf2a52aa2d7ad964')
    response2 = requests.get(url2).json()
    url2 = str(response2['articles'][0]['url'])
    title2 = str(response2['articles'][0]['title'])
    image_url2 = str(response2['articles'][0]['urlToImage'])



    context = {
        'url': url,
        'title': title,
        'image': image_url,
        'url2': url2,
        'title2': title2,
        'image2': image_url2
    }
    return render(request, 'news.html', context=context)

