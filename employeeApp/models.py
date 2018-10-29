from django.db import models
from syllabusApp.models import Syllabus, Course

# Create your models here.
type = (
    ('Teacher', 'Teacher'),
    ('Staff', 'Staff'),
)


class Employee(models.Model):
    emp_Id = models.AutoField(primary_key=True)
    emp_fullName = models.CharField(max_length=1000)
    emp_shortForm = models.CharField(max_length=500)
    emp_code = models.CharField(max_length=500, null=True, blank=True)
    emp_type = models.CharField(max_length=255, choices=type)
    emp_designation = models.CharField(max_length=255)
    emp_priority = models.IntegerField(default=0)
    emp_password = models.CharField(max_length=255, default=36)
    emp_link = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.emp_shortForm


class CourseAssignTeacher(models.Model):
    courseAssignTeacher_Id = models.AutoField(primary_key=True)
    emp_Id_Fk = models.ForeignKey(Employee)
    courseAssignTeacher_syllabus_Id_Fk = models.ForeignKey(Syllabus)
    courseAssignTeacher_course_Id_Fk = models.ForeignKey(Course)

    # def __str__(self):
    #     return self.emp_Id_Fk.emp_shortForm


class PriorityHandling(models.Model):
    priorityHandling_Id = models.AutoField(primary_key=True)
    emp_teacher_Id_Fk = models.ForeignKey(Employee)
    priority_start = models.CharField(max_length=500)
    priority_end = models.CharField(max_length=500)
    priority_status = models.CharField(max_length=500)

    def __str__(self):
        return self.emp_teacher_Id_Fk.emp_shortForm
