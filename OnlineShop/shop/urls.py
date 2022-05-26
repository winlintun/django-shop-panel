from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/', views.customer, name="customer"),
    path('product/', views.product, name='product'),
]