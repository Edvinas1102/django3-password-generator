from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('abcdefghijklmoprgsq')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMOPRSQTUVZXY'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))\

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    len = int(request.GET.get('length', 12))  # taken from home.html
    password = ''
    for x in range(len):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':password})


def about(request):
    return render(request, 'generator/about.html')