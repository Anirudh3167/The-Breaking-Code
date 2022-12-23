from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "Base_platform"
urlpatterns = [
    path('',Home,name="Home"),
    path('login/',Login,name="Login"),
    path('logout/',Logout,name="Logout"),
    path('about/',About,name="About"),
    path('terms/',Terms,name="Terms"),
    path('conditions/',Conditions,name="Conditions"),
    path('leafs/',Leafs,name="Leafs"),
    path('faq/',FAQ,name="FAQ"),
    path('help/',Help,name="Help"),
    path('profile/',Profile,name="Profile"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)