from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Client, Employee, Product, PhotoProduct, Order, OrderPosition

from .serializer import ClientSerializers, EmployeeSerializers, ProductSerializers, PhotoProductSerializers, \
    OrderSerializers, OrderPositionSerializers


class ClientAPIView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializers(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ClientSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientDetail(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerializers(client)
        return Response(serializer.data)

    def put(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerializers(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        client = self.get_object(pk)
        client.delete()
        return Response(status=204)


class EmployeeAPIView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializers(employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        employee = self.get_object(pk=pk)
        serializer = EmployeeSerializers(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        employee = self.get_object(pk=pk)
        serializer = EmployeeSerializers(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class PhotoProductAPIView(APIView):
    def get(self, request):
        photo_product = PhotoProduct.objects.all()
        serializer = PhotoProductSerializers(photo_product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PhotoProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return PhotoProduct.objects.get(pk=pk)
        except PhotoProduct.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        photo_product = self.get_object(pk=pk)
        serializer = PhotoProductSerializers(photo_product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        photo_product = self.get_object(pk=pk)
        serializer = PhotoProductSerializers(photo_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        photo_product = self.get_object(pk=pk)
        photo_product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
