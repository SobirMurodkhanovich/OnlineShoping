from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class PhotoProduct(models.Model):
    photo = models.CharField(max_length=10_000)

    def __str__(self):
        return self.photo


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField
    photo = models.OneToOneField(PhotoProduct, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    total_cost = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=(
        ('naqt', 'NAQT'),
        ('clic', 'CLIC'),
    ))

    def __str__(self):
        return self.employee


class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
