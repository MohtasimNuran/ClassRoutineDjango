from django.db import models

# Create your models here.

# class Syllabus(models.Model):
#     syllabus_Id = models.AutoField(primary_key=True)
#     syllabus_level = models.CharField(max_length=500)
#     syllabus_duration = models.CharField(max_length=1000)
#
#     def __str__(self):
#         return "%s-%s-%s"% (self.syllabus_Id, self.syllabus_level, self.syllabus_duration)


# Create your models here.
# semesters = (
#     ('1st Semester', '1st Semester'),
#     ('2nd Semester', '2nd Semester'),
#     ('3rd Semester', '3rd Semester'),
#     ('4th Semester', '4th Semester'),
#     ('5th Semester', '5th Semester'),
#     ('6th Semester', '6th Semester'),
#     ('7th Semester', '7th Semester'),
#     ('8th Semester', '8th Semester'),
#
# )
academic_Level = (
    ('Bachelor of Science (B.Sc.)', 'Bachelor of Science (B.Sc.)'),
    ('Master of Science (M.Sc.)', 'Master of Science (M.Sc.)'),
)


class Syllabus(models.Model):
    syl_session = models.CharField(max_length=500)

    def __str__(self):
        return self.syl_session


class Level(models.Model):
    lvl_name = models.CharField(max_length=500, choices=academic_Level)

    def __str__(self):
        return self.lvl_name


class Semester(models.Model):
    semester_name = models.CharField(max_length=500)
    level_Id = models.ForeignKey(Level)

    def __str__(self):
        return self.semester_name


class Course(models.Model):
    course_code = models.CharField(max_length=500, blank=True)
    course_name = models.CharField(max_length=500, blank=True)
    course_credit = models.CharField(max_length=500, blank=True)
    semester_Id = models.ForeignKey(Semester)
    level_Id = models.ForeignKey(Level)
    syl_Id = models.ForeignKey(Syllabus)

    def __str__(self):
        return '%s--- %s' % (self.course_code, self.course_name)
