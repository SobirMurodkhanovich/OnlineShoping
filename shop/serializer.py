from rest_framework import serializers
from .models import Product, Order, OrderPosition


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class OrderPositionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderPosition
        fields = ['id', 'product', 'quantity', 'get_cost']
        read_only_fields = ['get_cost']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        product, created = Product.objects.get_or_create(**product_data)
        order_position = OrderPosition.objects.create(product=product, **validated_data)
        return order_position


class OrderSerializer(serializers.ModelSerializer):
    positions = OrderPositionSerializer(many=True)
    total_cost = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    date_time = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'positions_', 'total_cost', 'date_time']

    def create(self, validated_data):
        positions_data = validated_data.pop('positions_')
        order = Order.objects.create()
        for position_data in positions_data:
            product_data = position_data.pop('product')
            product, created = Product.objects.get_or_create(**product_data)
            OrderPosition.objects.create(order=order, product=product, **position_data)
        order.calculate_total_cost()
        return order

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions_', None)

        if positions_data is not None:
            instance.positions.all().delete()
            for position_data in positions_data:
                product_data = position_data.pop('product')
                product, created = Product.objects.get_or_create(**product_data)
                OrderPosition.objects.create(order=instance, product=product, **position_data)

        instance.calculate_total_cost()
        return instance
