from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,"Eco_Info/home.html")

def Blogs(request):
    return render(request,"Eco_Info/Blogs/index.html")

def Learn(request):
    return render(request,"Eco_Info/Learn/index.html")