from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Order, OrderPosition

from .serializer import ProductSerializers, \
    OrderSerializers, OrderPositionSerializers


class ProductAPIView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderPositionAPIView(APIView):
    def get(self, request):
        order_position = OrderPosition.objects.all()
        serializer = OrderPositionSerializers(order_position, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderPositionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderPositionDetailAPIView(APIView):
    def get_object(self, request, pk):
        try:
            return OrderPosition.objects.get(pk=pk)
        except OrderPosition.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        order_position = self.get_object(pk=pk)
        serializer = OrderPositionSerializers(order_position)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order_position = self.get_object(pk=pk)
        serializer = OrderPositionSerializers(order_position, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order_position = self.get_object(pk=pk)
        order_position.delete()


class OrderAPIView(APIView):
    def get(self, request):
        order = Order.objects.all()
        serializer = OrderSerializers(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPIView(APIView):
    def get_object(self, request, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        order = self.get_object(pk=pk)
        serializer = OrderSerializers(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        order = self.get_object(pk=pk)
        serializer = OrderSerializers(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_object(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
