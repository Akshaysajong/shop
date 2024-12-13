from django.shortcuts import render, redirect
from adminapp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def homepage(request):
    product = Product.objects.all()
    cart = request.session.get('cart', {})
    total_quantity = sum(item['quantity'] for item in cart.values())
    print('cart:', cart)
    context = {
        'product': product,
        'cart_quantity': total_quantity,
    }
    
    return render(request, 'shop/homepage.html', context)

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('name:', first_name)
        customer = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
    return render(request, 'shop/signup.html')

def login_customer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active and not user.is_superuser:
                login(request, user) 
                return redirect('home-page')
    return render(request, 'shop/login_customer.html')

def add_to_cart_view(request,id):
    product = Product.objects.get(id=id)
    print('product:', product) 
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)]['quantity'] += 1
    else:
        cart[str(id)] = {
            'name': product.name,
            'price': str(product.price),
            'description': product.description,
            'image': product.image.url,
            'quantity': 1
        }
    request.session['cart'] = cart
    return redirect('home-page')

def cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    context = {
        'cart': cart, 
        'total_price': total_price,
    }
    return render(request, 'shop/cart.html', context)

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
        request.session['cart'] = cart
    return redirect('cart')

@login_required(login_url='login-customer')
def placed_order(request):
    user = request.user
    print('user:', user)
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    if request.method == 'POST':
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('postal_code')
        phone = request.POST.get('phone')

        address = Address.objects.create(user=user, address=address, city=city, state=state, postal_code=pin, phone=phone)
        for product_id, item in cart.items():
            product = Product.objects.get(id=product_id)
            Orders.objects.create(address=address,product=product,status='Pending', total=total_price)

        if 'cart' in request.session:
            del request.session['cart'] 
            
    return render(request, 'shop/customer_address.html')


@login_required(login_url='login-customer')
def my_order(request):
    user_id = request.user.id
    user = Address.objects.filter(user=user_id)
    orders=[]
    for x in user:
        order = Orders.objects.filter(address=x.id)
        print('or:',order)
        orders.append(order)
        ordered_products = []
        for order in order:
            print(order)
            ordered_product=Product.objects.all().filter(id=order.product.id)
            ordered_products.append(ordered_product)
        # print('product:', ordered_products)
    context = {
        'data':zip(ordered_products,orders)
    }
    return render(request, 'shop/my_order.html', context)