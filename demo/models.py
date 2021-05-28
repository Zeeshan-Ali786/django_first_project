from django.db import models

# Create your models here.


class StudentID(models.Model):
    batch = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=10, blank=True)
    department = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.batch


class Student(models.Model):
    first_name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=10, blank=True)
    father_name = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to='image/', blank=True)
    date_of_birth = models.DateField(blank=True)
    gender = models.BooleanField(blank=True)
    email_address = models.EmailField(blank=True)
    batch = models.OneToOneField(StudentID, null=True, blank=True, on_delete=models.CASCADE,)

    def __str__(self):
        return self.first_name


class Character(models.Model):
    department = models.CharField(max_length=10, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='characters', blank=True)
    # ForeignKey  is used for a connection between Student Class and  Character Class

    def __str__(self):
        return self.department


class Department(models.Model):
    department_name = models.CharField(max_length=10, blank=True)
    department_abbreviation = models.CharField(max_length=50, blank=True)
    students = models.ManyToManyField(Student, related_name='department', blank=True)

    # one student studying in only one Batch but one Batch have many students

    def __str__(self):
        return self.department_name
