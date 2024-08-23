from django.contrib import admin
from .models import OrderPosition, Product, Order
# Register your models here.
admin.site.register(OrderPosition)
admin.site.register(Product)
admin.site.register(Order)