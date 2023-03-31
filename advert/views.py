from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from django.contrib.auth.decorators import login_required
from .forms  import *

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    paginate_by = 5
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     users = User.objects.count()
    #     context = {
    #         'users': users
    #     }

    #     return context
    
    #     print(context)
    

@login_required(login_url='signin')
def cart(request):
    return render(request, 'cart.html')

@login_required(login_url='signin')
def checkout(request):
    return render(request, 'checkout.html')

@login_required(login_url='signin')
def orders(request):
    return render(request, 'orders.html')

@login_required(login_url='signin')
class ProductCreateView(CreateView):
    model = Product
    template_name = 'post.html'
    form_class = PostProductForm
    success_url = reverse_lazy('home')
