from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from User.forms import RegistrationForm, AccountAuthenticationForm, MoneyTransferForm
from User.models import Account, Transaction_List
import requests
from django.views.generic import ListView
from pycoingecko import CoinGeckoAPI


# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            date_of_birth = form.cleaned_data.get('date_of_birth')
            full_name = form.cleaned_data.get('full_name')
            address = form.cleaned_data.get('address')
            country = form.cleaned_data.get('country')
            account = authenticate(
                email=email,
                password=raw_password,
                date_of_birth=date_of_birth,
                full_name=full_name,
                address=address,
                country=country,
            )
            login(request, account)
            return redirect("/")
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'User/register.html', context)



def login_form(request):
    context = {}
    
    user = request.user
    if user.is_authenticated:
        return redirect("/login")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            
            if user:
                login(request, user)
                return redirect('/')
            
    else:
        form = AccountAuthenticationForm()
        
    context['login_form'] = form
    
    return render(request, 'User/login.html', context)




def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    # NEWS
    url = ('https://newsapi.org/v2/everything?'
        'q=Business&'
        'from=2022-09-02&'
        'sortBy=popularity&'
        'apiKey=5fa0d0485aa5497d9fde386421fa8609')

    response = requests.get(url).json()
    article = response['articles']
         
    Crypto = ('https://newsapi.org/v2/everything?'
        'q=Bitcoin&'
        'from=2022-09-02&'
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
    return render(request, 'User/home.html', context=context)


# CONVERT IT TO CBV[HOPEFULLY I CAN UNDERSTAND IT]       

def bank_view(request):   
    queryset = Transaction_List.objects.all()
    
    if request.method == 'POST':
        
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
            
            
            SENDER_IBAN = Account.objects.get(IBAN=request.user.IBAN) # IBAN
            
            RECEIVER_IBAN_FORM = form.cleaned_data['receiver_IBAN']
            RECEIVER_IBAN = Account.objects.get(IBAN=RECEIVER_IBAN_FORM)
            
            AMOUNT = form.cleaned_data['amount']
            if SENDER_IBAN.balance < AMOUNT:
                pass # Made with html that you cant surpass user.balance, might use as secondhand proofing
            
            SENDER_IBAN.balance = SENDER_IBAN.balance - AMOUNT
            
            RECEIVER_IBAN.balance = RECEIVER_IBAN.balance + AMOUNT
            
            SENDER_IBAN.save()
            RECEIVER_IBAN.save()
            return redirect('/bank/')
            
    else:
        form = MoneyTransferForm()
    context= {'transaction_listas': queryset}
    return render(request, 'User/bank.html', context)
