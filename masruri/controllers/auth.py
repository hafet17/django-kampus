from django.shortcuts import render, redirect

def loginPage (request):
    context = {
     'judul': 'Halaman Login',
     'menu': 'login',
    }
    return render(request, 'auth/login.html', context)

def registerPage (request):
    context = {
     'judul': 'Halaman Register',
     'menu': 'register',
    }
    return render(request, 'auth/register.html', context)