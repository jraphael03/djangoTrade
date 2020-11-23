from django.shortcuts import render

# Create your views here.
def home( request):
    import requests
    import json
    
    #pk_d498d40ec96e4e1d8bb7a6e68424254d   (iexstockAPIkey)
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_d498d40ec96e4e1d8bb7a6e68424254d")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render( request, 'home.html', {'api' : api})

def about( request):
    return render( request, 'about.html', {})


