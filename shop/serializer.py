from rest_framework import serializers
from .models import Client, Employee, Product, PhotoProduct, Order, OrderPosition


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PhotoProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhotoProduct
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderPositionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderPosition
        fields = '__all__'

