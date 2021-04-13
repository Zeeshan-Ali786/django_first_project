from django.db import models

# Create your models here.
class Student(models.Model):
    First_Name = models.CharField(max_length=10, unique=True)
    Last_Name = models.CharField(max_length=10, unique=True)
    Father_Name = models.CharField(max_length=10, unique=True)
    Image = models.ImageField(upload_to='image/', blank=True)
    Date_of_Birth = models.DateField()
    Gender = models.BooleanField()
    Email = models.EmailField()


    def __str__(self):
        return self.First_Name
