from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, status
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

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
# Custom Methods

    @action(detail=True, methods=['POST'])
    def rate_student(self, request, pk=None):
        # request data
        if 'stars' in request.data:
            response = {'message': 'its working'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'you need to provide stars inside body'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )
