from django.shortcuts import render, redirect
from . models import Stock
from .forms import StockForm
from django.contrib import messages


# Create your views here.
def home( request):
    import requests
    import json    #json is used to parse
        #connect to api, bring data to app, parse it, do something with it

    if request.method == "POST" and "getStockData" in request.POST:
        ticker = request.POST['ticker']   #ticker is the name of the form so whatever this is the form inputs
        #pk_d498d40ec96e4e1d8bb7a6e68424254d   (iexstockAPIkey)
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")
            
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render( request, 'home.html', {'api' : api})

    else:
        return render( request, 'home.html', {})

    if request.method == "POST" and "addStockBtn" in request.POST:
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('add_stock')

    else:
        #pull object out of database
        ticker = Stock.object.all()
        output = []  #empty list so we can append api's
        for ticker_item in ticker:

            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) +"/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render( request,  'add_stock.html', {'ticker' : ticker, 'output' : output})

def about( request):
    return render( request, 'about.html', {})

def add_stock( request):
    import requests
    import json

    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('add_stock')

    else:
        #pull object out of database
        ticker = Stock.objects.all()    #our model is Stock
        output = []   #empty list so we can append api's
        for ticker_item in ticker:    #loops through each item and makes an api call for each
            
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) +"/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")
                
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error..."
        return render( request, 'add_stock.html', {'ticker' : ticker, 'output' : output})  #pass in the ticker

def delete( request, stock_id):
    item = Stock.objects.get(pk=stock_id)   #primarykey = stock_id so we can capture specific element
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(add_stock)


def delete_stock( request):
    ticker = Stock.objects.all()    #our model is Stock
    return render( request, 'delete_stock.html', {'ticker' : ticker})

def test( request):
    if request.method == "POST":
        ticker = request.POST['ticker']   #ticker is the name of the form so whatever this is the form inputs
        #pk_d498d40ec96e4e1d8bb7a6e68424254d   (iexstockAPIkey)
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")
            
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
    return render( request, 'test.html', {'api' : api})

    return render( request, 'test.html', {})