from django.db import models
from syllabusApp.models import Syllabus
from examApp.models import Exam

halls = (
    ('SRJ', 'SRJ'),
    ('MH', 'MH'),
    ('Vashani', 'Vashani'),
    ('Bangobondhu', 'Bangobondhu'),
    ('Khaleda Zia', 'Khaleda Zia'),
)
gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)
dept = (
    ('CSE', 'CSE'),
    ('IIT', 'IIT'),
)


# Create your models here.

class Student(models.Model):
    std_Id = models.AutoField(primary_key=True)
    std_fullName = models.CharField(max_length=1000)
    std_dept = models.CharField(max_length=1000, choices=dept)
    std_classRoll = models.CharField(max_length=500)
    std_examRoll = models.CharField(max_length=1000)
    std_registrationNumber = models.CharField(max_length=1000)
    std_phone = models.CharField(max_length=255)
    std_hall = models.CharField(max_length=500, choices=halls)
    std_session = models.CharField(max_length=255)
    std_gender = models.CharField(max_length=500, choices=gender)

    # std_code = models.Value(std_session+"-"+std_classRoll+"-"+std_dept)

    def __str__(self):
        return self.std_fullName


class CourseEnrollment(models.Model):
    courseEnrollment_Id = models.AutoField(primary_key=True)
    std_Id_Fk = models.ForeignKey(Student)
    courseEnrollment_syllabus_Id_Fk = models.ForeignKey(Syllabus)
    courseEnrollment_exam_Id_Fk = models.ForeignKey(Exam)

    def __str__(self):
        return self.courseEnrollment_Id
