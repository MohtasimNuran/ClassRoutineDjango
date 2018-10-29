from syllabusApp.models import Course
from django.forms import ModelForm

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_code','course_name', 'course_credit', 'semester_Id', 'level_Id', 'syl_Id']