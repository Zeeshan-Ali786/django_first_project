from django.contrib import admin
from .models import Student
# from .views import temp
# Register your models here.
# admin.register(temp)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # fields = ['Father_Name','Gender']
    list_display = ['First_Name','Last_Name','Father_Name','Image','Date_of_Birth','Gender','Email']
    # list_filter = ['Email']
    search_fields = ['First_Name']


