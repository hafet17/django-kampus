from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
# Create your views here.


def home(request):
    data = {
        'judul': 'Halaman Dashboard',
        'menu': 'home'
    }
    return render(request, 'dashboard.html', data)


def products(request):
    data = {
        'judul': 'Halaman Produk',
        'menu': 'products'
    }
    return render(request, 'products.html', data)


def custumer(request):
    data = {
        'judul': 'Halaman Customer',
        'menu': 'custumer'
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
