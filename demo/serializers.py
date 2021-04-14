from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'First_Name', 'Last_Name', 'Father_Name', 'Gender', 'Date_of_Birth']