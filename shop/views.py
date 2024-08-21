from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from .models import Client, Employee, Product, PhotoProduct, Order, OrderPosition
from .serializer import ClientSerializers, EmployeeSerializers, ProductSerializers, PhotoProductSerializers, \
    OrderSerializers, OrderPositionSerializers


# Create your views here.

class ClientCreateAPIView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


class ClientListAPIView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


class ClientDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


class EmployeeCreateAPIView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class EmployeeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PhotoProduct.objects.all()
    serializer_class = PhotoProductSerializers


class PhotoProductCreateAPIView(CreateAPIView):
    queryset = PhotoProduct.objects.all()
    serializer_class = PhotoProductSerializers


class PhotoProductListAPIView(ListAPIView):
    queryset = PhotoProduct.objects.all()
    serializer_class = PhotoProductSerializers


class PhotoProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PhotoProduct.objects.all()
    serializer_class = PhotoProductSerializers


class OrderCreateAPIView(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderListAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderPositionCreateAPIView(CreateAPIView):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializers


class OrderPositionListAPIView(ListAPIView):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializers


class OrderPositionDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializers
