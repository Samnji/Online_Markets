from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from .models import *
from django.contrib.auth.decorators import login_required
from .forms  import *
from django.http  import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger
from django.utils import timezone

 
class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    paginate_by = 5
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     users = User.objects.count()

    #     unordered_products = Order.objects.filter(ordered=False)

    #     if is_unordered.exists():

    #         order_items = items
    #         total_products = Order.items.count() * 

    #     context = {
    #         'users': users
    #     }

    #     return context
    
    #     print(context)
    
def search(request):
    category = request.GET.get('category')

    try:
        price = int(request.GET.get('price'))
    except ValueError:
        messages.info(request, "The price must be initialized with a number")

        return render(request, 'search.html')

    print(category)
    print(type(price))

    if category and price == 0:
        category_results = Product.objects.filter(category=category)

    elif category and price > 0:
        
        for price in range(price-3000, price+3000):
            category_results = Product.objects.filter(category=category, new_price=price)
            print(category_results)
    
    paginator = Paginator(category_results, 5)  # Display 5 items per page
    page = request.GET.get('page')
    try:
        category_results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        category_results = paginator.page(1)

    context = {

        'category_results': category_results,
    }

    return render(request, 'search.html', context)

@login_required(login_url='signin')
def add_to_cart(request, product_id):
    context = {}
    # Check if the product exists and get its fields
    product = get_object_or_404(Product, id=product_id)

    # Check if product is in product order and add item into product order if not
    product_order, created = ProductOrder.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )
    # Check if there is still an order that has not yet been ordered
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # Check if the product order is in the order
        if order.items.filter(product=product_id):
            product_order.quantity  += 1
            product_order.save

            messages.success(request, f"{product.name} quantity has been added to your cart!")

            return redirect('cart')
        else:
            order.items.add(product_order)

            messages.success(request, f"{product.name} has been added to your cart!")

            return redirect('home')

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user,
            ordered_date=ordered_date,
            )

        order.items.add(product_order)

        messages.success(request, f"Your order has been created and {product.name} added to your cart!")

        return redirect('home')

@login_required(login_url='signin')
def cart(request):
    unordered_products = Order.objects.filter(user=request.user, ordered=False)
    product_orders = ProductOrder.objects.filter(user=request.user)
    if unordered_products.exists():
        total_products = ProductOrder.objects.count() 

        context = {
            'product_orders': product_orders,
            'total_products': total_products
        }
    
        return render(request, 'cart.html', context)

    else:
        messages.info(request, "You haven't added any product into cart yet")

        return render(request, 'cart.html')


@login_required(login_url='signin')
def checkout(request):
    return render(request, 'checkout.html')

@login_required(login_url='signin')
def orders(request):
    return render(request, 'orders.html')

@login_required(login_url='signin')
def postProduct(request):
    if request.method == 'POST':
        form = PostProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()

            messages.success(request, "Your product has been posted successfully")

            return HttpResponseRedirect(reverse('post'))

    return render(request, 'post.html')


