from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('forgot_pass/', forgot_pass, name='forgot_pass'),
    path('change_pass/', change_pass, name='change_pass'),
]
