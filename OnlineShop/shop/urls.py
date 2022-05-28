from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<int:user_id>/', views.customer, name="customer"),
    path('product/', views.product, name='product'),
    path('order/create/<int:customerId>/', views.orderCreate, name='order-create'),
    path('order/update/<int:orderId>', views.order_update, name='order-update'),
    path('order/delete/<int:orderId>/', views.order_delete, name="order-delete"),
]