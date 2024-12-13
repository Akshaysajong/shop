from rest_framework import serializers
from adminapp.models import *
from shopapp.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']


class CustomerSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'order_date', 'total_amount', 'status']
    
