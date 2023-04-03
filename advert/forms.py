from django import forms
from .models import *

class PostProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'old_price', 'new_price')
    