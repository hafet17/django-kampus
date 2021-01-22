from django.shortcuts import render, redirect
from masruri.forms import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from masruri.decorators import tolakhalaman_ini, ijinkan_pengguna


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin'])
def index(request):

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
