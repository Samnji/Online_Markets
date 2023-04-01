from django import forms
from .models import *

class PostProductForm(forms.ModelForm):
    # name = forms.CharField(max_length = 100)
    # description = forms.CharField(max_length = 500)
    # image = forms.ImageField()
    # category = forms.CharField(max_length=50)
    # old_price = forms.IntegerField()
    # new_price = forms.IntegerField()

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'old_price', 'new_price')