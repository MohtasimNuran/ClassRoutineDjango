from django.contrib import admin
from studentApp.models import Student, CourseEnrollment

# Register your models here.

admin.site.register(Student)

admin.site.register(CourseEnrollment)