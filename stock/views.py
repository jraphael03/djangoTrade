from django.shortcuts import render

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


