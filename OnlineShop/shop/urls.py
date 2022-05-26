from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<int:user_id>/', views.customer, name="customer"),
    path('product/', views.product, name='product'),
    path('order/create/', views.orderCreate, name='order-create'),
]