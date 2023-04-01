from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
    path('post/', postProduct, name='post'),
    path('search/', search, name='search'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
