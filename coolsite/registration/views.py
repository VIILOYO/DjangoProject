from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


def RegisterPage(request):
    """Регистрация пользователя"""
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('first_name')
                messages.success(request, f'Вы зарегестрировались, {user}.')

                return redirect('login')

        context = {
            'title': 'Регистрация',
            'form': form,
        }

        return render(request, 'registration/register.html', context=context)


def LoginPage(request):
    """Авторизация пользователя"""
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('HomePage')
            else:
                messages.info(request, 'Почта или пароль неверны.')
        context = {'title': 'Авторизация'}
        return render(request, 'registration/login.html', context=context)


def LogoutUser(request):
    """Выход пользователя"""
    logout(request)
    return redirect('HomePage')
