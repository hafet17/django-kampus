from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from masruri.filters import OrderFilter


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


# ========== views Product ============



# ========== views custumer ===========



def student(request):

    student = Student.objects.all()
    data = {
        'judul': 'Halaman Student',
        'menu': 'student',
        'student': student
    }
    return render(request, 'student.html', data)


def createOrder(request):

    formOrder = OrderForm()
    if request.method == 'POST':
        formsimpan = OrderForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
    data = {
        'judul': 'Form Order',
        'form': formOrder
    }
    return render(request, 'order/order_form.html', data)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    formorder = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = OrderForm(request.POST, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('/')
    context = {
        'judul': 'Edit Order',
        'form': formorder,
    }
    return render(request, 'order/order_form.html', context)


def deleteOrder(request, pk):

    orderhapus = Order.objects.get(id=pk)
    if request.method == 'POST':
        orderhapus.delete()
        return redirect('/')

    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete': orderhapus,
    }
    return render(request, 'order/delete_form.html', context)
