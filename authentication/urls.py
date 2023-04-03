from django.urls import path
from .views import *
from advert.encrypt_url import urlEncryption, urlEncoding

urlpatterns = [
    path(f"{urlEncryption('signin')}{urlEncoding('signin')}/", signin, name='signin'),
    path(f"{urlEncryption('signup')}{urlEncoding('signup')}/", signup, name='signup'),
    path(f"{urlEncryption('logout')}{urlEncoding('logout')}/", logout, name='logout'),
    path(f"{urlEncryption('forgot_pass')}{urlEncoding('forgot_pass')}/", forgot_pass, name='forgot_pass'),
    path(f"{urlEncryption('change_pass')}{urlEncoding('change_pass')}/", change_pass, name='change_pass'),
]
