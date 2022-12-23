from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request):
    return render(request,'Eco_Store/storeHome.html')
    
def Product(request):
    return render(request,"Eco_Store/product_details.html")

def ProdCategories(request):
    return render(request,"Eco_Store/storeHome_categories.html")