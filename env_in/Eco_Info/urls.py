from django.urls import path
from .views import *

app_name = "Eco_Info"
urlpatterns = [
    path('',Home,name="Home"),
    path('blogs/',Blogs,name="Blogs"),
    path('learn/',Learn,name="Learn"),
]
