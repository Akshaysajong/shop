from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('signup/', CustomerSignupView.as_view(), name='customer-signup'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('orders/', UserOrderListView.as_view(), name='user-orders'),
]