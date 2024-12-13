from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import *

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user.is_superuser:
            login(request, user)
            return redirect('customer-list')
    return render(request, 'admin/login.html')

def customerlist(request):
    customer_list = User.objects.filter(is_superuser = '0')
    context = {
        'customer_list': customer_list,
    }
    return render(request, 'admin/customerlist.html', context)


def addproduct(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        pic = request.FILES.get('pic')
        print(name)
        product = Product.objects.create(
            name = name,
            description = description,
            price = price,
            image = pic
        )
        return redirect('product-list') 
    return render(request, 'admin/addproduct.html')

def productlist(request):
    product_list = Product.objects.all()
    context = {
        'product_list' : product_list
    }
    return render(request, 'admin/productlist.html', context)

def editproduct(request):
    # if request.method == "GET":
    id = request.GET.get('a')
    product = Product.objects.get(id=id)
    print('product:', product)
    context = {
        'product': product,
    }
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        pic = request.FILES.get('image')
        print('pic:', pic)
        if 'image' in request.FILES:
            print('++++++++++++++++++++++++++')
            product.image = request.FILES.get('image')
        product.save()
        return redirect('product-list')    

    return render(request, 'admin/editproduct.html', context)

def deleteproduct(request):
    id = request.GET.get('a')
    print('id:', id)
    Product.objects.filter(id=id).delete()
    return redirect('product-list')

def orders(request):
    return render(request, 'admin/orderlist.html')