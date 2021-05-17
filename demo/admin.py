from django.contrib import admin
from .models import Student, StudentID, Character, Batch
# from .views import temp
# Register your models here.
# admin.register(temp)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # fields = ['Father_Name','Gender']
    list_display = ['first_name', 'last_name', 'father_name', 'image', 'date_of_birth', 'gender', 'email_address']
    # list_filter = ['Email']
    search_fields = ['first_name']


admin.site.register(StudentID)
admin.site.register(Character)
admin.site.register(Batch)

