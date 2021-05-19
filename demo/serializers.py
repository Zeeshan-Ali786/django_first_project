from rest_framework import serializers
from .models import Student, StudentID, Character, Department


class StudentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentID
        fields = ['id', 'batch', 'roll_no', 'department']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'department']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name', 'department_abbreviation']


class StudentSerializer(serializers.ModelSerializer):
    batch = StudentIDSerializer(many=False)
    characters = CharacterSerializer(many=True)
    department = DepartmentSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'father_name', 'gender', 'date_of_birth', 'batch', 'characters', 'department']