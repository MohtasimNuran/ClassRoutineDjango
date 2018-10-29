from django.shortcuts import render, HttpResponse
from studentApp.forms import StudentForm, CourseEnrollmentForm
from studentApp.models import Student


# Create your views here.

def addStudent_view(request):
    if request.POST:
        form = StudentForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = StudentForm
        return render(request, 'addStudent.html', {'form': form})


def courseEnrollment_view(request):
    if request.POST:
        form = CourseEnrollmentForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = CourseEnrollmentForm
        return render(request, 'courseEnrollment.html', {'form': form})


def studentList_view(request):
    if request.GET:
        session = request.GET.get('session')
        studentList = Student.objects.filter(std_session=session)
        sessionList = Student.objects.all()
        return render(request, 'studentList.html', {'sessionList': sessionList, 'studentList': studentList})
    else:
        sessionList = Student.objects.all()
        return render(request, 'studentList.html', {'sessionList': sessionList})
