# views.py
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # Your view logic here
    context = {"variable_name": "Hello, Django!"}
    return HttpResponse("This is home page")
