from django.shortcuts import render, redirect
from masruri.forms import *
from django.contrib.auth.decorators import login_required
from masruri.decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login


@login_required(login_url='login')
# @ijinkan_pengguna(yang_diizinkan=['admin'])
@pilihan_login
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
