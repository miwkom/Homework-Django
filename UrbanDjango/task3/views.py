from django.shortcuts import render
from django.views.generic import TemplateView


def platform(request):
    return render(request, 'platform.html')


def games(request):
    return render(request, 'games.html')


def cart(request):
    return render(request, 'cart.html')
