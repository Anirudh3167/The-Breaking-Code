from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .rapyd_apis import make_request

# Create your views here.
def Home(request):
    return render(request,'Eco_Store/storeHome.html')
    
def Product(request):
    if request.method == "POST":
        return redirect("Eco_Store:Cart")
    return render(request,"Eco_Store/product_details.html")

def ProdCategories(request):
    return render(request,"Eco_Store/storeHome_categories.html")

def Cart(request):
    return render(request,"Eco_Store/storeCart.html")


@login_required(login_url='Login')
def PaymentDirection(request):
    wallet_body = {
        "amount": 50,
        "currency": "USD",
        "country":"US",
        "complete_payment_url":"Eco_Sotre:Home",
        #Change this github link at the time of production. to the website link
        #Rapyd do not allow urls of local host. Thats why we kept github here
        "complete_checkout_url":"https://www.github.com/anirudh3167",
        "error_payment_url":"store:Failed"
    }
    response = make_request(method='post',path='/v1/checkout',body=wallet_body)
    #print(response)
    hosted_url = response['data']['redirect_url']
    #print("REDIRECT_URL:",hosted_url)
    return redirect(hosted_url)
