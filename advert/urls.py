from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from .encrypt_url import urlEncryption, urlEncoding

urlpatterns = [
    # Encrypting and encoding urls to prevent url bruteforce attack
    path(f"{urlEncryption('cart')}{urlEncoding('cart')}/", cart, name='cart'),
    path(f"{urlEncryption('checkout')}{urlEncoding('checkout')}/", checkout, name='checkout'),
    path(f"{urlEncryption('orders')}{urlEncoding('orders')}/", orders, name='orders'),
    path(f"{urlEncryption('post')}{urlEncoding('post')}/", postProduct, name='post'),
    path(f"{urlEncryption('search')}{urlEncoding('search')}/", search, name='search'),
    path(f"{urlEncryption('add_to_cart')}{urlEncoding('add_to_cart')}/<int:product_id>/", add_to_cart, name='add_to_cart'),
    path(f"{urlEncryption('remove_from_cart')}{urlEncoding('remove_from_cart')}/<int:product_id>/", remove_from_cart, name='remove_from_cart'),
    path(f"{urlEncryption('reduce_from_cart')}{urlEncoding('reduce_from_cart')}/<int:product_id>/", reduce_from_cart, name='reduce_from_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
