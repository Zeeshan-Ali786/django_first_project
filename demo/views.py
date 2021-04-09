from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class Third(View):
    def get(self, request):
        return HttpResponse('This is another function inside class')

def First(request):
    return HttpResponse('First message from views')

def Second(request):
    return HttpResponse('Second message')

def Third(request):
    return HttpResponse('Third message')





