from django.shortcuts import redirect, render
from .models import Customer, Product, Order
from .forms import OrderForm
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

    return render(request, 'shop/customer.html', {
        'customer': customer,
        'orders': orders,
        'order_count': order_count
    })

def product(request):
    products = Product.objects.all()
    return render(request, 'shop/product.html', {
        'products': products
    })

def orderCreate(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:home')
    return render(request, 'shop/order_form.html', {
        'form': form
    })