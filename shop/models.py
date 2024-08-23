from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.date_time}"

    def calculate_total_cost(self):
        total = sum(position.get_cost() for position in self.positions.all())
        self.total_cost = total
        self.save()


class OrderPosition(models.Model):
    order = models.ForeignKey(Order, related_name='positions_', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_positions_', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    def get_cost(self):
        return self.product.price * self.quantity
