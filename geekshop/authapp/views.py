from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.urls import reverse
from basket.models import Basket


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
        form = UserLoginForm()

    content = {'title': 'Geekshop | Авторизация',
               'form': form}
    return render(request, 'authapp/login.html', content)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы зарегистрированы')
            return HttpResponseRedirect(reverse('authapp:login'))

        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    content = {'title': 'Geekshop | Регистрация',
               'form': form}
    return render(request, 'authapp/register.html', content)


@login_required
def profile(request):
    user_select = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили свои данные')
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=user_select)
    content = {'title': 'Geekshop | Профиль',
               'form': form,
               'baskets': Basket.objects.filter(user=user_select)}
    return render(request, 'authapp/profile.html', content)


def logout(request):
    auth.logout(request)
    return render(request, 'mainapp/index.html')
