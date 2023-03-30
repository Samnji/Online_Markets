from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
    path('post/', post, name='post'),
]
