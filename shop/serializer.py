from rest_framework import serializers
from .models import Product, Order, OrderPosition


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = '__all__'
