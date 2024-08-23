from rest_framework import viewsets
from .models import Product, Order, OrderPosition
from .serializer import ProductSerializer, OrderSerializer, OrderPositionSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderPositionViewSet(viewsets.ModelViewSet):
    queryset = OrderPosition.objects.all()
    serializer_class = OrderPositionSerializer
