from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def First(request):
    return HttpResponse('First message from views')

def Second(request):
    return HttpResponse('Second message from views')


