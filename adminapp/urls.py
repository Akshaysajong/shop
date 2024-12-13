from django.urls import path
from . import views

urlpatterns = [
    path('login-user/', views.login_user, name='login_user'),
    path('customer-list/', views.customerlist, name='customer-list'),
    path('add-product/', views.addproduct, name='add-product'),
    path('product-list/', views.productlist, name='product-list'),
    path('edit-product/', views.editproduct, name='edit-product'),
    path('delete-product/', views.deleteproduct, name='delete-product'),
    path('orders/', views.orders, name='orders'),
]