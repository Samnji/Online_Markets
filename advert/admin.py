from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)
admin.site.register(County)
admin.site.register(Shipping)