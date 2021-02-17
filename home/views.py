from django.shortcuts import render

# Create your views here.

def home(requests):
    return render(requests, 'home/welcome.html')

def mydash(requets):
    return render(requets, 'home/mydash.html')
