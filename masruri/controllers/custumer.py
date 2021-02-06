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


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['custumer'])
def accountSetting(request):
    datacustumer = request.user.custumer
    form = CustumerForm(instance=datacustumer)
    if request.method == 'POST':
        form = CustumerForm(request.POST, request.FILES, instance=datacustumer)
        if form.is_valid:
            form.save()
    context = {
        'menu': 'settings',
        'formcustumer': form
    }
    return render(request, 'auth/account.html', context)
