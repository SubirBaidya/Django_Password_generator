from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    charecters = list('abcdefghijklmopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charecters.extend('ABCDEFGHIJKLMOPQRSTUVWXYZ')

    if request.GET.get('numbers'):
        charecters.extend('123456789')

    if request.GET.get('special'):
        charecters.extend('!@#$%^&*()_+')



    length = int(request.GET.get('length'))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(charecters)

    return render(request, 'generator/password.html', {'password': thepassword})
