from django.shortcuts import render, redirect
from . models import Stock
from .forms import StockForm
from django.contrib import messages


# Create your views here.
def home( request):
    import requests
    import json
    
    if request.method == "POST":
        ticker = request.POST['ticker']   #ticker is the name of the form so whatever this is the form inputs
        #pk_d498d40ec96e4e1d8bb7a6e68424254d   (iexstockAPIkey)
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")
            
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render( request, 'home.html', {'api' : api})

    else:
        return render( request, 'home.html', {'ticker' : 'Enter a ticker symbol above'})




def about( request):
    return render( request, 'about.html', {})


def add_stock( request):
    if request.method == "POST":
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added!"))
            return redirect('add_stock')

    else:
        #pull object out of database
        ticker = Stock.objects.all()    #our model is Stock
        return render( request, 'add_stock.html', {'ticker' : ticker})  #pass in the ticker

def delete( request, stock_id):
    item = Stock.objects.get(pk=stock_id)   #primarykey = stock_id so we can capture specific element
    item.delete()
    messages.success(request, ("Stock Has Been Deleted!"))
    return redirect(add_stock)


