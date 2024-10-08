from django.shortcuts import render
from .forms import UserRegistrationForm


def sign_up_by_django(request):
    users = ['user1', 'user2', 'user3']
    context = {
        'info': '',
        'error': ''
    }
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                context['error'] = 'Пароли не совпадают!'
            elif len(password) < 8:
                context['error'] = 'Пароль должен быть не менее 8 символов!'
            elif username in users:
                context['error'] = 'Логин занят!'
            elif int(age) < 18:
                context['error'] = 'Вы не достигли 18 лет!'
            else:
                users.append(username)
                context['info'] = f'Регистрация завершена,{username}!'
    else:
        form = UserRegistrationForm()
    return render(request, 'registration_page.html', context)


def sign_up_by_html(request):
    users = ['user1', 'user2', 'user3']
    context = {
        'form': '',
        'error': ''
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if username and password and repeat_password and age:
            if password != repeat_password:
                context['error'] = 'Пароли не совпадают!'
            elif len(password) < 8:
                context['error'] = 'Пароль должен быть не менее 8 символов!'
            elif username in users:
                context['error'] = 'Логин занят!'
            elif int(age) < 18:
                context['error'] = 'Вы не достигли 18 лет!'
            else:
                users.append(username)
                context['info'] = f'Регистрация завершена,{username}!'
        else:
            context['error'] = 'Заполните все пустые поля!'
    return render(request, 'registration_page.html', context)