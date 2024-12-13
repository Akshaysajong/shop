from django.urls import path
from . import views

urlpatterns = [
   path('', views.homepage, name='home-page'),
   path('signup/', views.signup, name='signup'),
   path('login-customer/', views.login_customer, name='login-customer'),
   path('add-to-cart/<int:id>', views.add_to_cart_view,name='add-to-cart'),
   path('cart/', views.cart, name='cart'),
   path('remove_from_cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
   path('placed_order/', views.placed_order, name='placed-order'),
   path('my_order/', views.my_order, name='my-order'),
]
