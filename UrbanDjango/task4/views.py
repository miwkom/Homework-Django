from django.shortcuts import render


def platform(request):
    title = 'Главное меню'
    context = {
        'title' : title
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Витрина'
    games = ["Arma 3", "Baldur's Gate 3", "Elden Ring", "No Man's Sky", "Rimworld"]
    context = {
        'title': title,
        'content': games
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'cart.html', context)
