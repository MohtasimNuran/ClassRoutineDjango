from django.db import models
from examApp.models import Exam
from othersApp.models import ClassRoom, ClassTime
from employeeApp.models import CourseAssignTeacher
from syllabusApp.models import Course

# Create your models here.
days = (
    ('Sat', 'Sat'),
    ('Sun', 'Sun'),
    ('Mon', 'Mon'),
    ('Tues', 'Tues'),
    ('Wed', 'Wed'),
    ('Thurs', 'Thurs'),
    ('Fri', 'Fri'),
)


class EndClass(models.Model):
    endclass_Id = models.AutoField(primary_key=True)
    exam_Id_FK = models.ForeignKey(Exam)
    startingDate = models.CharField(max_length=1000)
    endingDate = models.CharField(max_length=1000, null=True, blank=True)
    classHeldWeek = models.CharField(max_length=500)

    def __str__(self):
        return 'Starting Date : %s, Ending Date : %s' % (self.startingDate, self.endingDate)


class ClassRoutine(models.Model):
    classRoutine_Id = models.AutoField(primary_key=True)
    assignedTeacher_Fk = models.ForeignKey(CourseAssignTeacher)
    course_Id_Fk = models.ForeignKey(Course)
    classTime_Id_Fk = models.ForeignKey(ClassTime)
    classRoom_Id_Fk = models.ForeignKey(ClassRoom)
    dayOfWeek = models.CharField(max_length=500)
    semesterTry = models.CharField(max_length=500, default='1st')
    teacher_Id = models.IntegerField(default=0)

    # def __str__(self):
    #     return self.classTime_Id_Fk
    def __str__(self):
        return 'Teacher : %s, Course : %s, Time : %s' % (self.assignedTeacher_Fk, self.course_Id_Fk, self.classTime_Id_Fk)
