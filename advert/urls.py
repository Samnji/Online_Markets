from django.urls import path
from .views import *
from .views import (
    ProductCreateView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
    path('post/', ProductCreateView.as_view(), name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
