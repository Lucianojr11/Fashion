from django.shortcuts import render
from django.http import HttpResponse
from moda.models import main

# Create your views here.


def index(request):
    prod = main.objects.all()
    return render(request, 'index.html', {"produto": prod})