from django.db import models


# Create your models here.

class Exam(models.Model):
    exam_Id = models.AutoField(primary_key=True)
    exam_code = models.CharField(max_length=500)
    exam_year = models.CharField(max_length=500)
    exam_student_year = models.CharField(max_length=500)
    exam_student_semester = models.CharField(max_length=500)

    def __str__(self):
        return self.exam_code
