from django.shortcuts import render

def home_screen_view(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def orders(request):
    return render(request, 'orders.html')

def post(request):
    return render(request, 'post.html')
