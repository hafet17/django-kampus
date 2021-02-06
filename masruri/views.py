from django.shortcuts import render, redirect
from . forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from masruri.filters import OrderFilter


def student(request):

    student = Student.objects.all()
    data = {
        'judul': 'Halaman Student',
        'menu': 'student',
        'student': student
    }
    return render(request, 'student.html', data)
