from django.contrib import admin
from .models import OrderPosition, Product
# Register your models here.
admin.site.register(OrderPosition)
admin.site.register(Product)