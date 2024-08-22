from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),

    path('order_position/', OrderPositionAPIView.as_view()),
    path('order_position/<int:pk>/', OrderPositionDetailAPIView.as_view()),

    path('order/', OrderAPIView.as_view()),
    path('order/<int:pk>/', OrderDetailAPIView.as_view()),

]
