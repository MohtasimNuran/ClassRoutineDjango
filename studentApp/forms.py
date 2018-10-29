from studentApp.models import Student, CourseEnrollment
from django.forms import ModelForm


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['std_fullName', 'std_dept', 'std_classRoll', 'std_examRoll', 'std_registrationNumber', 'std_phone',
                  'std_hall', 'std_session', 'std_gender']
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['std_fullName'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_dept'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_classRoll'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_examRoll'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_registrationNumber'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_hall'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_session'].widget.attrs.update({'class': 'form-control'})
        self.fields['std_gender'].widget.attrs.update({'class': 'form-control'})

class CourseEnrollmentForm(ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = ['std_Id_Fk', 'courseEnrollment_syllabus_Id_Fk', 'courseEnrollment_exam_Id_Fk']
    def __init__(self, *args, **kwargs):
        super(CourseEnrollmentForm, self).__init__(*args, **kwargs)
        self.fields['std_Id_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['courseEnrollment_syllabus_Id_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['courseEnrollment_exam_Id_Fk'].widget.attrs.update({'class': 'form-control'})