from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.


def home(request):

    list_custumer = Custumer.objects.all()
    list_order = Order.objects.all()
    total_order = list_order.count()
    delivered = list_order.filter(status='Deliverd').count()
    pending = list_order.filter(status='Pending').count()

    data = {
        'judul': 'Halaman Dashboard',
        'menu': 'home',
        'custumer': list_custumer,
        'order': list_order,
        'total_orders': total_order,
        'delivered': delivered,
        'pending': pending,
    }
    return render(request, 'dashboard.html', data)


def products(request):

    list_product = Product.objects.all()

    data = {
        'judul': 'Halaman Produk',
        'menu': 'products',
        'product': list_product,
    }
    return render(request, 'products.html', data)


def custumer(request, pk):

    detailcustumer = Custumer.objects.get(id=pk)
    order_custumer = detailcustumer.order_set.all()
    total_custumer = order_custumer.count()

    data = {
        'judul': 'Halaman Customer',
        'menu': 'custumer',
        'custumer': detailcustumer,
        'order_custumer': order_custumer,
        'total_custumer': total_custumer
    }
    return render(request, 'customer.html', data)


def student(request):

    student = Student.objects.all()
    data = {
        'judul': 'Halaman Student',
        'menu': 'student',
        'student': student
    }
    return render(request, 'student.html', data)
