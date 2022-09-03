import requests
import json

def home():
    url = ('https://newsapi.org/v2/everything?'
        'q=Apple&'
        'from=2022-09-02&'
        'sortBy=popularity&'
        'apiKey=5fa0d0485aa5497d9fde386421fa8609')


    result = []
    response = requests.get(url).json()
    article = response['articles']
    print(article[3]['url'])
    

    
home()