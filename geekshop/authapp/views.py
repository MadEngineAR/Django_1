from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import UserLoginForm, UserRegisterForm
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print('Пользователь неактивен')
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    content = {'title': 'Geekshop | Авторизация',
               'form': form}
    return render(request, 'authapp/login.html', content)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))

        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    content = {'title': 'Geekshop | Регистрация',
               'form': form}
    return render(request, 'authapp/register.html', content)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
