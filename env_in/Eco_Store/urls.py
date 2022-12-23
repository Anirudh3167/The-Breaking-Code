from django.urls import path
from .views import *

app_name = "Eco_Store"
urlpatterns = [
    path('',Home,name="Home"),
    path('prod/',Product,name="Product"),
    path('prod-cat/',ProdCategories,name="ProductCategories"),
    path('cart/',Cart,name="Cart"),
    path('pay-direct/',PaymentDirection,name="Checkout"),
    path('reused/',Reused,name="Reused"),
]
