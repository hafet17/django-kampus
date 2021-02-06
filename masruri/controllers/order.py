from django.shortcuts import render, redirect
from masruri.forms import Order, OrderForm
from masruri.decorators import tolakhalaman_ini, ijinkan_pengguna


@ijinkan_pengguna(yang_diizinkan=['admin'])
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


@ijinkan_pengguna(yang_diizinkan=['admin'])
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


@ijinkan_pengguna(yang_diizinkan=['admin'])
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
