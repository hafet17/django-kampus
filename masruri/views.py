from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

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

def products(request):

    search_product = request.GET.get('q')

    if search_product:
        product = Product.objects.filter(name=search_product)
    else:
        # If not searched, return default posts
        product = Product.objects.all().order_by("-date_created")

    paginator = Paginator(product, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'judul': 'Halaman Produk',
        'menu': 'products',
        'page_obj': page_obj
    }
    return render(request, 'product/index.html', data)


def createProducts(request):

    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Product baru berhasil ditambahkan")
            return redirect('/products')

    data = {
        'judul': 'Create Data Product',
        'form': form
    }

    return render(request, 'product/product_form.html', data)


def updateProducts(request, pk):

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Product Berhasil Di Update")
            return redirect('/products')

    data = {
        'judul': 'Update Data Product',
        'form': form
    }

    return render(request, 'product/product_form.html', data)


def deleteProducts(request, pk):

    delete_product = Product.objects.get(id=pk)
    if request.method == 'POST':
        delete_product.delete()
        messages.success(
            request, "Product Berhasil Di Hapus")
        return redirect('/products')

    data = {
        'judul': 'Delete Data Product',
        'deleteproduct': delete_product
    }
    return render(request, 'product/delete_form.html', data)


# ========== views custumer ===========
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
