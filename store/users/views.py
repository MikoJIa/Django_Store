from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import *
from django.contrib import auth, messages
from django.urls import reverse


# В этом контроллере будет работать два запроса
def login(request):
    if request.method == 'POST':  # Если зпост запрос
        form = UserLoginForm(data=request.POST)  # Мы вызываем класс и передоём параметр(передаём данные)-данные которые были заполнены в форме
        if form.is_valid():  # Проверяем данные на валидность
            username = request.POST['username']
            password = request.POST['password']
            # Объевляем переменную user
            # Тут происход проверка на существование пользователя в БД
            user = auth.authenticate(username=username, password=password)
            if user:  # Если пользователь есть то мы его авторизуем
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))  # Возвращаемся на главную страницу
            # Если нас перенаправило на главную страницу значит авторизация прошла успешно!
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Великолепно!!! Вы успешно зарегестрировались.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)  # передаём новые данные
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    context = {'title': 'Store-профиль', 'form': form}
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))