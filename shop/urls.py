from django.urls import path
from .views import *

urlpatterns = [
    path('client/', ClientAPIView.as_view()),
    path('client/<int:pk>/', ClientDetail.as_view()),

    path('employee/', EmployeeAPIView.as_view()),
    path('employee/<int:pk>/', EmployeeDetailAPIView.as_view()),

    path('photo_product/', PhotoProductAPIView.as_view()),
    path('photo_product/<int:pk>/', PhotoProductDetailAPIView.as_view()),

    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),

    path('order/', OrderAPIView.as_view()),
    path('order/<int:pk>/', OrderDetailAPIView.as_view()),

    path('order_position/', OrderPositionAPIView.as_view()),
    path('order_position/<int:pk>/', OrderPositionDetailAPIView.as_view()),

]
