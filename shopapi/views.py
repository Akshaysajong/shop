from rest_framework.views import APIView
from rest_framework.generics import  ListAPIView
from rest_framework.response import Response
from adminapp.models import Product
from shopapp.models import Address, Orders
from .serializers import ProductSerializer, CustomerSignupSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class LoginAPIView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Logged In successfully!",
                "token": token.key,
                "username": user.username,
                "email": user.email,
            }, status=status.HTTP_200_OK)
        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)


class CustomerSignupView(APIView):

    def post(self, request):
        serializer = CustomerSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Customer created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserOrderListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id=request.user
        address = Address.objects.filter(user=user_id)
        order_list = []
        for ad in address:
            orders = Orders.objects.filter(address=ad.id)
            for order in orders:
                order_list.append({
                    "id":order.id,
                    "product_name": order.product.name,
                    "price": order.total,
                    "created_at": order.order_date
                })
        return Response({"orders": order_list})