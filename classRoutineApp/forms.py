from django.forms import ModelForm, DateInput
from classRoutineApp.models import EndClass, ClassRoutine


class EndClassForm(ModelForm):
    class Meta:
        model = EndClass
        fields = ['exam_Id_FK', 'startingDate', 'endingDate', 'classHeldWeek']
        widgets = {
            'startingDate': DateInput(attrs={'type': 'date'})
        }
    def __init__(self, *args, **kwargs):
        super(EndClassForm, self).__init__(*args, **kwargs)
        self.fields['exam_Id_FK'].widget.attrs.update({'class': 'form-control'})
        self.fields['startingDate'].widget.attrs.update({'class': 'form-control'})
        self.fields['endingDate'].widget.attrs.update({'class': 'form-control'})
        self.fields['classHeldWeek'].widget.attrs.update({'class': 'form-control'})

class ClassRoutineForm(ModelForm):
    class Meta:
        model = ClassRoutine
        fields = ['assignedTeacher_Fk', 'course_Id_Fk', 'classTime_Id_Fk', 'classRoom_Id_Fk', 'dayOfWeek']
    def __init__(self, *args, **kwargs):
        super(ClassRoutineForm, self).__init__(*args, **kwargs)
        self.fields['assignedTeacher_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['course_Id_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['classTime_Id_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['classRoom_Id_Fk'].widget.attrs.update({'class': 'form-control'})
        self.fields['dayOfWeek'].widget.attrs.update({'class': 'form-control'})