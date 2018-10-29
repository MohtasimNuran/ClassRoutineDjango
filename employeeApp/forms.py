from employeeApp.models import Employee, CourseAssignTeacher
from django.forms import ModelForm


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_fullName', 'emp_shortForm', 'emp_code', 'emp_type', 'emp_designation', 'emp_priority', 'emp_password', 'emp_link']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['emp_fullName'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_shortForm'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_code'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_designation'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_priority'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['emp_link'].widget.attrs.update({'class': 'form-control'})


class CourseAssignTeacherForm(ModelForm):
    class Meta:
        model = CourseAssignTeacher
        fields = ['emp_Id_Fk', 'courseAssignTeacher_syllabus_Id_Fk', 'courseAssignTeacher_course_Id_Fk']

    def __init__(self, *args, **kwargs):
        super(CourseAssignTeacherForm, self).__init__(*args, **kwargs)
        self.fields['emp_Id_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['courseAssignTeacher_syllabus_Id_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['courseAssignTeacher_course_Id_Fk'].widget.attrs.update({'class': 'form-control'})