from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
#
# class Third(View):
#     students = Student.objects.all()
#     output = ''
#     # output = f"we have {len(students)} Students in Database"
#     for student in students:
#         output += f"We have {student.First_Name} as a student with ID {student.id}<br>"
#     def get(self, request):
#         return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')


def second(request):
    return HttpResponse('Second message')


def temp(request):
    students = Student.objects.all()
    return render(request, 'first_temp.html', {'data': 'This is Data inside views File And this is called Dynamic template'})
    # return render(request, 'first_temp.html', {'students': students})


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )