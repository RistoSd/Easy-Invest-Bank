import requests

def currency_exchange(sender_curr: str, reciever_curr: str, amount: int) -> int:
    """
    Takes sender currency and reciever currency and amount then
    converts the amount according to currencies provided.

    Params:
        sender_curr (str): the currency tied to the sender
        reciever_curr (str): the currency tied to the reciever
        amount (int): the amount to exchange
    Return:
        (str): rounded amount by 2 decimals
    """
    url = 'https://exchange-rates.abstractapi.com/v1/convert'
    querystring = {
        'api_key': 'c6982eecf09f4920af0a2b426ed3d252',
        'base': sender_curr,
        'target': reciever_curr,
        'base_amount': amount
    }
    response = requests.get(url, params=querystring).json()
    converted_amount = response.get('converted_amount')
    return round(converted_amount, 2)