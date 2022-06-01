from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Customer, Product, Order
from .forms import OrderForm, RegisterForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total = orders.count()
    delivered = Order.objects.filter(status='delivered').count()
    pending = Order.objects.filter(status='pending').count()

    return render(request, 'shop/home.html', {
        'customers': customers,
        'orders': orders,
        'total': total,
        'delivered': delivered,
        'pending': pending
    })


def customer(request, user_id):
    customer = Customer.objects.get(pk=user_id)

    orders = customer.order_set.all()
    order_count = orders.count()

    filter_obj = OrderFilter(request.GET, queryset=orders)
    orders = filter_obj.qs

    return render(request, 'shop/customer.html', {
        'customer': customer,
        'orders': orders,
        'order_count': order_count, 
        'filter_obj' : filter_obj,
    })


def product(request):
    products = Product.objects.all()
    return render(request, 'shop/product.html', {
        'products': products
    })


def orderCreate(request, customerId):
    customer = Customer.objects.get(pk=customerId)
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    formset = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('shop:home')
    return render(request, 'shop/order_form.html', {
        'formset': formset
    })


def order_update(request, orderId):
    order = Order.objects.get(pk=orderId)
    form = OrderForm(instance=order, queryset=Order.objects.none())
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    return render(request, 'shop/order_form.html', {
        'form': form
    })


def order_delete(request, orderId):
    order = Order.objects.get(pk=orderId)
    if request.method == 'POST':
        order.delete()
        return redirect('shop:home')
    return render(request, 'shop/order_delete.html', {
        'order': order
    })


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:home')

    return render(request, 'shop/register.html', {
        'form': form
    })