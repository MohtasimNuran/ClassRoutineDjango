from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import date, timedelta, datetime
from employeeApp.forms import CourseAssignTeacherForm, EmployeeForm
from employeeApp.models import CourseAssignTeacher, PriorityHandling, Employee


# Create your views here.
def addEmployee(request):
    if request.GET:
        form = EmployeeForm(data=request.GET)
        if form.is_valid():
            obj = form.save(commit=False)
            type = form['emp_type'].data
            designation = form['emp_designation'].data
            shortForm = form['emp_shortForm'].data
            obj.emp_code = type + designation + shortForm
            obj.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = EmployeeForm
        return render(request, 'addEmployee.html', {'form': form})


def courseAssignTeacher_view(request):
    if request.GET:
        form = CourseAssignTeacherForm(request.GET)
        courseAssignedTeacherDetailed = CourseAssignTeacher.objects.all().order_by('emp_Id_Fk')
        if form.is_valid():
            form.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = CourseAssignTeacherForm
        courseAssignedTeacherDetailed = CourseAssignTeacher.objects.all().order_by('emp_Id_Fk')
        return render(request, 'courseAssignTeacher.html',
                      {'form': form, 'teacherAssignDetails': courseAssignedTeacherDetailed})


# def passToNextTeacher(request):
#     if request.GET:
#         priorityHandling = PriorityHandling()
#         priorityHandling.emp_teacher_Id_Fk_id = request.GET.get('teacherId')
#         priorityHandling.priority_start = datetime.now()
#         priorityHandling.priority_end = datetime.now() + timedelta(hours=12)
#         priorityHandling.priority_status = 'active'
#         priorityHandling.save()
#         return HttpResponse("Done")
#     else:
#         return render(request, 'passToNextTeacher.html')




def loginEmployee(request):
    if request.GET:
        shortForm = request.GET.get('shortForm')
        password = request.GET.get('password')

        if Employee.objects.filter(emp_shortForm=shortForm, emp_password=password, emp_type='Teacher'):
            request.session['username'] = shortForm
            request.session['type'] = 'Teacher'
            return HttpResponseRedirect('/')
        elif Employee.objects.filter(emp_shortForm=shortForm, emp_password=password, emp_type='Staff'):
            request.session['username'] = shortForm
            request.session['type'] = 'Staff'
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("login failed")

    else:
        return render(request, 'loginEmployee.html')


def employeeList_view(request):
    teacherList = Employee.objects.filter(emp_type='Teacher')
    staffList = Employee.objects.filter(emp_type='Staff')
    return render(request, 'employeeList.html', {'teacherList': teacherList, 'staffList': staffList})


def activeRoutineByAdmin_view(request):
    priorityOneTeacher = Employee.objects.filter(emp_priority='1')
    for p in priorityOneTeacher:
        priorityTeacherId = p.emp_Id
    priorityHandling = PriorityHandling()
    priorityHandling.emp_teacher_Id_Fk_id = priorityTeacherId
    priorityHandling.priority_start = datetime.now()
    priorityHandling.priority_end = datetime.now() + timedelta(hours=12)
    priorityHandling.priority_status = 'active'
    priorityHandling.save()

    return HttpResponse("Routine Active")


def logoutEmployee(request):
    del request.session['username']
    return HttpResponseRedirect('/')
