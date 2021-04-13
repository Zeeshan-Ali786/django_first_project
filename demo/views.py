from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Student


# Create your views here.

class Third(View):
    students = Student.objects.all()
    output = ''
    # output = f"we have {len(students)} Students in Database"
    for student in students:
        output += f"We have {student.First_Name} as a student with ID {student.id}<br>"
    def get(self, request):
        return HttpResponse(self.output)

def First(request):
    return HttpResponse('First message from views')


def Second(request):
    return HttpResponse('Second message')

def temp(request):
    students = Student.objects.all()
    # return render(request, 'first_temp.html', {'data': 'This is Data inside views File And this is called Dynamic template'})
    return render(request, 'first_temp.html', {'students': students})
