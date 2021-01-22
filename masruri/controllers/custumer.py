from django.shortcuts import render, redirect
from masruri.forms import *
from django.core.paginator import Paginator
from masruri.filters import OrderFilter
from django.contrib.auth.decorators import login_required
from masruri.decorators import tolakhalaman_ini, ijinkan_pengguna


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def index(request, pk):

    detailcustumer = Custumer.objects.get(id=pk)
    order_custumer = detailcustumer.order_set.all()
    total_custumer = order_custumer.count()
    filter_order = OrderFilter(request.GET, queryset=order_custumer)
    order_custumer = filter_order.qs

    halaman_tampil = Paginator(order_custumer, 2)
    halaman_url = request.GET.get('halaman', 1)
    halaman_order = halaman_tampil.get_page(halaman_url)

    if halaman_order.has_previous():
        url_previous = f'?halaman={halaman_order.previous_page_number()}'
    else:
        url_previous = ''
    if halaman_order.has_next():
        url_next = f'?halaman={halaman_order.next_page_number()}'
    else:
        url_next = ''

    data = {
        'judul': 'Halaman Customer',
        'menu': 'custumer',
        'custumer': detailcustumer,
        'order_custumer': order_custumer,
        'total_custumer': total_custumer,
        'filter_data_order': filter_order,
        'halaman_order_custumer': halaman_order,
        'previous': url_previous,
        'next': url_next
    }
    return render(request, 'customer.html', data)
