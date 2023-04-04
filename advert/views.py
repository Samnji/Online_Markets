from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from .models import *
from django.contrib.auth.decorators import login_required
from .forms  import *
from django.http  import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.contrib.auth import authenticate

def calculateTotal(request):
    unordered_products = Order.objects.filter(user=request.user, ordered=False)
    product_orders = ProductOrder.objects.filter(user=request.user, ordered=False)

    # Check if there are unordered products and calculate their quantinty and total price
    if unordered_products.exists(): 
        total_products_quantity = 0
        total_products_price = 0


        for product_order in product_orders:

            total_products_quantity += product_order.quantity
            total_products_price += product_order.quantity * product_order.product.new_price

    
        return (product_orders, total_products_quantity, total_products_price)


def productList(request):
    products = Product.objects.all()

    # All active users
    users = User.objects.count()
    orders = Order.objects.filter(ordered=True).count()
    context = {
        'users': users,
        'orders': orders,
    }
    # Check if the user has logined into their account and show the unordered products alonside the cart
    if request.user.is_authenticated:
        unordered_products = Order.objects.filter(user=request.user, ordered=False)
        
        if unordered_products.exists():
            product_orders, total_products_quantity, total_products_price = calculateTotal(request)

            context['total_products_price'] = total_products_price
            context['product_orders'] = product_orders,
            context['total_products_quantity'] = total_products_quantity

    # Check if there are products to showcase or not
    if products.exists():
        # Pagination
        paginator = Paginator(products, 5)

        page = request.GET.get('page')

        try:
            products = paginator.page(page)

        except PageNotAnInteger:
            products = paginator.page(1)

        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products

        return render(request, "home.html", context)
        
    else:
        messages.info(request, "There are no products yet. Post to add products.")

        return render(request, "home.html", context)
    
def search(request):
    context = {}
    category = request.GET.get('category')

    try:
        price = int(request.GET.get('price'))
    except ValueError:

        messages.info(request, "The price must be initialized with a number")

        return render(request, 'search.html', context)

    if category and price == 0:
        category_results = Product.objects.filter(category=category)

    elif category and price > 0:
        category_results = Product.objects.filter(category=category).filter(new_price__gte=price-3000).filter(new_price__lte=price+3000)
    
    else:
        messages
    paginator = Paginator(category_results, 5)  # Display 5 items per page
    page = request.GET.get('page')
    try:
        category_results = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        category_results = paginator.page(1)
    except EmptyPage:
            category_results = paginator.page(paginator.num_pages)

    context['category_results'] = category_results
    
    # Check if the user has logined into their account and show the unordered products alonside the cart
    if request.user.is_authenticated:
        unordered_products = Order.objects.filter(user=request.user, ordered=False)
        
        if unordered_products.exists():
            product_orders, total_products_quantity, total_products_price = calculateTotal(request)

            context['total_products_price'] = total_products_price
            context['product_orders'] = product_orders,
            context['total_products_quantity'] = total_products_quantity

    return render(request, 'search.html', context)

    


@login_required(login_url='signin')
def cart(request):
    unordered_products = Order.objects.filter(user=request.user, ordered=False)
    counties = County.objects.all()
    
    if unordered_products.exists():
        product_orders, total_products_quantity, total_products_price = calculateTotal(request)

        context = {
            'total_products_price': total_products_price,
            'product_orders': product_orders,
            'total_products_quantity': total_products_quantity,
            'counties': counties,
        }
        
        if request.method == 'POST':
            if 'promo_code' in request.POST:        
                promo_code = request.POST['promo_code']

                if promo_code == "This is the promo code":
                    context['total_products_price'] -= 1000

                    saved_info = Shipping.objects.filter(user=request.user, save_info=True)
                    if saved_info.exists():
                        save_info = True
                        context['save_info'] = save_info
                        context['saved_info'] = saved_info

                    messages.success(request, "Hurraay! The promo code was correct and the total price of your products have been reduced by Ksh 1000")

                    return render(request, 'checkout.html', context)

                else:
                    messages.info(request, f"The promo code was incorrect and the total price of your products is still {total_products_price}")

                    return render(request, 'cart.html', context)

            else:

                return render(request, 'checkout.html', context)
        return render(request, 'cart.html', context)

    else:
        messages.info(request, "You haven't added any product into cart yet")

        return render(request, 'cart.html')
    

@login_required(login_url='signin')
def add_to_cart(request, product_id):
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
            product_order.save()

            messages.success(request, f"{product.name} quantity has been added in your cart!")

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

        messages.success(request, f"Your order has been created and {product.name} added to your cart")

        return redirect('home')

@login_required(login_url='signin')
def remove_from_cart(request, product_id):
    # Check if the product exists and get its fields
    product = get_object_or_404(Product, id=product_id)
    product_order = ProductOrder.objects.get(product=product, ordered=False)
    product_order.delete()
    messages.info(request, f"{product.name} removed from your cart.")

    return redirect('cart')
    
@login_required(login_url='signin')
def reduce_from_cart(request, product_id):
    # Check if the product exists and get its fields
    product = get_object_or_404(Product, id=product_id)

    # Check if there is still an order that has not yet been ordered
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # Check if the product order is in the order
        if order.items.filter(product=product_id):
            product_order = ProductOrder.objects.filter(
                    user=request.user,
                    product=product,
                    ordered=False,

                )[0]
            if product_order.quantity > 1:
                product_order.quantity  -= 1
                product_order.save()
                
                messages.success(request, f"{product.name} quantity has been reduced in your cart.")

                return redirect('cart')
            
            elif product_order.quantity == 1:
                # Check if the product exists and get its fields
                product = get_object_or_404(Product, id=product_id)
                product_order = ProductOrder.objects.get(product=product, ordered=False)
                product_order.delete()
                messages.info(request, f"{product.name} removed from your cart.")

                return redirect('cart')

            else:
                messages.info(request, f"You can't reduce {product.name}'s quantity any more.")

                return redirect('cart')
        else:
            messages.info(request, f"{product.name} wasn't to your cart!")

            return redirect('cart')

    else:
        messages.info(request, f"You don't have an active order!")

        return redirect('home')


@login_required(login_url='signin')
def checkout(request):
    context = {}

    product_orders, total_products_quantity, total_products_price = calculateTotal(request)
    counties = County.objects.all()

    context = {
        'total_products_price': total_products_price,
        'product_orders': product_orders,
        'total_products_quantity': total_products_quantity,
        'counties': counties,
    }
    saved_info = Shipping.objects.filter(user=request.user, save_info=True)
    if saved_info.exists():
        save_info = True
        context['save_info'] = save_info
        context['saved_info'] = saved_info

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        county = request.POST['county']

        if 'save_info' in request.POST:
            save_info = True

        else:
            save_info = False
        
        user = User.objects.get(username=request.user)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Checking if the user shipping details exists and update
        if Shipping.objects.filter(user=request.user).exists():
            user_shipping_details = Shipping.objects.get(user=request.user)
            user_shipping_details.phone_number = phone_number
            user_shipping_details.address = address
            user_shipping_details.county = county
            user_shipping_details.save_info = save_info
            user_shipping_details.save()
        else:
            Shipping.objects.create(
                user=request.user,
                phone_number=phone_number,
                address=address,
                county =county,
                save_info=save_info,
            )

        
        # Check if there is any product that unordered then assign ordered
        if product_orders.exists():
            for unordered_product_order in product_orders:
                unordered_product_order.ordered = True
                unordered_product_order.save()
        
        # Check if there is still an order that has not yet been ordered
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            order.ordered = True
            order.save()

        return HttpResponseRedirect(reverse('orders'))

    return render(request, 'checkout.html', context)

@login_required(login_url='signin')
def orders(request):
    context = {}
    ordered_products = Order.objects.filter(user=request.user, ordered=True).order_by('-id')
    unordered_products = Order.objects.filter(user=request.user, ordered=False)
    
    # Show number of items in the cart link
    if unordered_products.exists():
        product_orders, total_products_quantity, total_products_price = calculateTotal(request)

        context = {
            'total_products_price': total_products_price,
            'product_orders': product_orders,
            'total_products_quantity': total_products_quantity,
        }

    if ordered_products.exists():
        order_items = []

        paginator = Paginator(ordered_products, 2)

        page = request.GET.get('page')

        try:
            orders = paginator.page(page)

        except PageNotAnInteger:
            orders = paginator.page(1)

        except EmptyPage:
            orders = paginator.page(paginator.num_pages)

        context['orders'] = orders


        return render(request, 'orders.html', context)
    else:
        messages.info(request, "You haven't made an order yet!")

        return render(request, 'orders.html')

@login_required(login_url='signin')
def postProduct(request):
    context = {}
    unordered_products = Order.objects.filter(user=request.user, ordered=False)
    
    # Show number of items in the cart link
    if unordered_products.exists():
        product_orders, total_products_quantity, total_products_price = calculateTotal(request)

        context = {
            'total_products_price': total_products_price,
            'product_orders': product_orders,
            'total_products_quantity': total_products_quantity,
        }

    if request.method == 'POST':
        form = PostProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()

            messages.success(request, "Your product has been posted successfully")

            return HttpResponseRedirect(reverse('post'))

    return render(request, 'post.html', context)

