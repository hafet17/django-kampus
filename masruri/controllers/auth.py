from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from masruri.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from masruri.decorators import tolakhalaman_ini
from django.contrib.auth.models import Group


@tolakhalaman_ini
def registerPage (request):
    formregister = RegisterForm()
    if request.method == 'POST':
        formregister = RegisterForm(request.POST)
        if formregister.is_valid():
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_custumer = formregister.save()
            grup = Group.objects.get(name='custumer')
            group_custumer.groups.add(grup)
            # formregister.save()
        return redirect('login')

    context = {
     'judul': 'Halaman Register',
     'menu': 'register',
     'tampilregister': formregister
    }
    return render(request, 'auth/register.html', context)

@tolakhalaman_ini
def loginPage (request):
    formlogin = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        validate = authenticate(request, username=username, password=password)
        if validate is not None:
            login(request, validate)
        return redirect('home')
    context = {
     'judul': 'Halaman Login',
     'menu': 'login',
     'tampillogin': formlogin
    }
    return render(request, 'auth/login.html', context)

def userPage(request):
    context = {}
    return render(request, 'auth/user.html', context)

def logoutPage(request):
     logout(request)
     return redirect('login')

