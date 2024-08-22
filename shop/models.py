from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name


class Order(models.Model):
    total_cost = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    order_position = models.ForeignKey(OrderPosition, on_delete=models.SET_NULL, null=True, blank=True)
