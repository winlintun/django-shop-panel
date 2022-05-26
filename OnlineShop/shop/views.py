from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer, Product
# Create your views here.

def home(request):
    return render(request, 'shop/home.html')

def customer(request):
    return render(request, 'shop/customer.html')

def product(request):
    products = Product.objects.all()
    return render(request, 'shop/product.html', {
        'products': products
    })