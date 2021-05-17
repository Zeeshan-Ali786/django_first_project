from rest_framework import serializers
from .models import Student, StudentID, Character, Batch


class StudentIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentID
        fields = ['id', 'isbn_10', 'isbn_12']


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'batch']


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['id', 'batch_name', 'batch_abbreviation']


class StudentSerializer(serializers.ModelSerializer):
    number = StudentIDSerializer(many=False)
    characters = CharacterSerializer(many=True)
    batch = BatchSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'father_name', 'gender', 'date_of_birth', 'number', 'characters', 'batch']