from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.forms.models import model_to_dict

# assigning User as our User model i.e. as User_details
User = get_user_model()

# Create your views here.
def Home(request):
    return render(request,"Base_platform/Home_Page.html")

def About(request):
    return render(request,"Base_platform/about.html")

def Terms(request):
    return render(request,"Base_platform/terms.html")

def Conditions(request):
    return render(request,"Base_platform/conditions.html")

def Login(request):
    if request.method == 'POST':
        if (request.POST['form-type'] == 'Login'):
            username = request.POST['UserName']
            password = request.POST['Password']
            new_user = authenticate(username=username,password=password)
            if new_user is not None:
                login(request,new_user)

            #getting the url
            try:
                return redirect(request.GET["next"])
            except:
                return redirect("Base_platform:Home")
                
        if (request.POST['form-type'] == 'Register'):
            #Basic User details.
            username = request.POST['UserName']
            email = request.POST['Email']
            password = request.POST['Password']
            new_user = User.objects.create_user(username=username,email=email,password=password)
            new_user.save()
            login(request,new_user)
            return redirect('Base_platform:Home')
    return render(request,"Base_platform/LoginPage.html")

def Logout(request):
    logout(request)
    return redirect('Base_platform:Home')

def Leafs(request):
    return render(request,"Eco_Store/Redeem/index.html")

def Help(request):
  return render(request,'Base_platform/FAQ.html')

def FAQ(request):
  return render(request,'Base_platform/FAQ.html')

def Profile(request):
    return render(request,"Base_platform/Profile.html")