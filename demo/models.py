from django.db import models

# Create your models here.


class StudentID(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_12 = models.CharField(max_length=12, blank=True)


class Student(models.Model):
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    father_name = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='image/', blank=True)
    date_of_birth = models.DateField()
    gender = models.BooleanField()
    email_address = models.EmailField()
    number = models.OneToOneField(StudentID, null=True, blank=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.first_name


class Character(models.Model):
    batch = models.CharField(max_length=10)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='characters')
    # ForeignKey  is used for a connection between Student Class and  Character Class

    def __str__(self):
        return self.batch


class Batch(models.Model):
    batch_name = models.CharField(max_length=10)
    batch_abbreviation = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, related_name='batch')

    # one student studying in only one Batch but one Batch have many students

    def __str__(self):
        return self.batch_name
