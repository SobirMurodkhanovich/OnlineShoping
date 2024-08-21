from django.urls import path
from .views import *

urlpatterns = [
    path('client/create/', ClientCreateAPIView.as_view()),
    path('client/list/', ClientListAPIView.as_view()),
    path('client/<int:pk>/', ClientDetailAPIView.as_view()),

    path('employee/create/', EmployeeCreateAPIView.as_view()),
    path('employee/list/', EmployeeListAPIView.as_view()),
    path('employee/<int:pk>/', EmployeeDetailAPIView.as_view()),

    path('photo_product/create/', PhotoProductCreateAPIView.as_view()),
    path('photo_product/list/', PhotoProductListAPIView.as_view()),
    path('photo_product/<int:pk>/', PhotoProductDetailAPIView.as_view()),

    path('product/create/', ProductCreateAPIView.as_view()),
    path('product/list/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),

    path('order/create/', OrderCreateAPIView.as_view()),
    path('order/list/', OrderListAPIView.as_view()),
    path('order/<int:pk>/', OrderDetailAPIView.as_view()),

    path('order_position/create/', OrderPositionCreateAPIView.as_view()),
    path('order_position/list/', OrderPositionListAPIView.as_view()),
    path('order_position/<int:pk>/', OrderPositionDetailAPIView.as_view()),
]
