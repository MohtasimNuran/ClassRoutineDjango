from django.shortcuts import render, HttpResponse
from classRoutineApp.forms import EndClassForm, ClassRoutineForm
from classRoutineApp.models import ClassRoutine, EndClass
from othersApp.models import Holiday
from syllabusApp.models import Syllabus, Course
from employeeApp.models import PriorityHandling, Employee, CourseAssignTeacher
from datetime import date, timedelta, datetime
from othersApp.models import ClassRoom, ClassTime
from django.db.models import Count
from examApp.models import Exam

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors


# Create your views here.

# def calculateClassEndingDate_view(request):
#     if request.GET:
#         # holidays = calculateHolidays(request)
#         sumDay = 0
#         form = EndClassForm(data=request.GET)
#         if form.is_valid():
#             startDate = form['startingDate'].value()
#             week = form['classHeldWeek'].value()
#             daysFromWeek = 7 * int(week)
#             classStartDate = datetime.strptime(startDate, '%Y-%m-%d')
#             classEndDate = classStartDate + timedelta(days=daysFromWeek)
#
#             allHoliday = Holiday.objects.all()
#             for a in allHoliday:
#                 if (datetime.strptime(a.holidayStart_date, '%Y-%m-%d') >= classStartDate) and (
#                             classEndDate >= datetime.strptime(a.holidayStart_date, '%Y-%m-%d')):
#                     classEndDate = classEndDate + timedelta(days=int(a.holidayInDays))
#
#                     # sumDay = sumDay + int(a.holidayInDays)
#                     # FinalDate = classEndDate + timedelta(days=int(sumDay))
#             obj = form.save(commit=False)
#             obj.endingDate = classEndDate
#             obj.save()
#             # formnew = EndClassForm(request.GET.copy())
#             # formnew.endingDate = classEndDate
#             # formnew.save()
#             return HttpResponse("Saved")
#         else:
#             return HttpResponse("Form is not valid")
#     else:
#         form = EndClassForm
#         return render(request, 'calculateClassEndingDate.html', {'form': form})

def calculateClassEndingDate_view(request):
    if request.GET:
        sumDay = 0
        startDate = request.GET.get('startDate')
        week = request.GET.get('week')
        daysFromWeek = 7 * int(week)
        classStartDate = datetime.strptime(startDate, "%Y-%m-%d").date()
        classEndDate = classStartDate + timedelta(days=daysFromWeek)

        allHoliday = Holiday.objects.all()
        for a in allHoliday:
            if (datetime.strptime(a.holidayStart_date, '%Y-%m-%d').date() >= classStartDate) and (
                        classEndDate >= datetime.strptime(a.holidayStart_date, '%Y-%m-%d').date()):
                classEndDate = classEndDate + timedelta(days=int(a.holidayInDays))

        endclass = EndClass()
        endclass.startingDate = startDate
        endclass.classHeldWeek = week
        endclass.exam_Id_FK_id = request.GET.get('exam')
        endclass.endingDate = classEndDate
        endclass.save()
        return HttpResponse("Saved")

    else:
        examList = Exam.objects.all()
        return render(request, 'calculateClassEndingDate.html', {'examList': examList})


def calculateHolidays(request):
    holidayStart = datetime.strptime(request.GET.get('holidayStart'), '%Y-%m-%d')
    holidayEnd = datetime.strptime(request.GET.get('holidayEnd'), '%Y-%m-%d')
    if holidayStart <= holidayEnd:
        dayLeft = (holidayEnd - holidayStart) + timedelta(days=1)
        return dayLeft


def classEndingDateList_view(request):
    endClassList = EndClass.objects.all()
    return render(request, 'viewClassEndingDate.html', {'endClassList': endClassList})


# def classRoutine_view(request):
#     if request.GET:
#         form = ClassRoutineForm(data=request.GET)
#         if form.is_valid():
#             if ClassRoutine.objects.filter(dayOfWeek=form['dayOfWeek'].data,
#                                            classRoom_Id_Fk=form['classRoom_Id_Fk'].data,
#                                            classTime_Id_Fk=form['classTime_Id_Fk'].data):
#                 return HttpResponse("Time and Day is already taken")
#             else:
#                 teacherId = CourseAssignTeacher.objects.filter(
#                     courseAssignTeacher_Id=form['assignedTeacher_Fk'].data).values('emp_Id_Fk')
#                 teacherPriority = Employee.objects.filter(emp_Id=teacherId).first()
#                 hasValue = PriorityHandling.objects.filter(
#                     emp_teacher_Id_Fk__emp_priority=teacherPriority.emp_priority - 1)
#                 if hasValue.count() or teacherPriority.emp_priority == 1:
#                     form.save()
#                     return HttpResponse("Saved")
#                 else:
#                     return HttpResponse("You have not the permission to proceed")
#         else:
#             return HttpResponse("Form is not valid")
#     else:
#         form = ClassRoutineForm
#
#         # day = 'Sat'
#         # time = 3
#         # count = onLoadCompare(day, time)
#
#         fullRoutine = ClassRoutine.objects.filter()
#         return render(request, 'classRoutine.html', {'form': form, 'fullRoutine': fullRoutine})


def classRoutine_view(request):
    if request.GET:

        assignedTeacherId = Employee.objects.filter(emp_shortForm=request.session['username'])
        for i in assignedTeacherId:
            teacherMainId = i.emp_Id
        # if PriorityHandling.objects.filter(emp_teacher_Id_Fk=teacherId - 1):

        course = Course.objects.filter(id=request.GET.get('course'))

        for s in course:
            semester = s.semester_Id.semester_name

        if ClassRoutine.objects.filter(dayOfWeek=request.GET.get('days'),
                                       classRoom_Id_Fk=request.GET.get('room'),
                                       classTime_Id_Fk=request.GET.get('classTime')):
            return HttpResponse("Time and Day is already taken")

        elif ClassRoutine.objects.filter(dayOfWeek=request.GET.get('days'),
                                         classTime_Id_Fk=request.GET.get('classTime'), semesterTry=semester):
            return HttpResponse("Students are busy in this schedule")
        elif ClassRoutine.objects.filter(dayOfWeek=request.GET.get('days'),
                                         classTime_Id_Fk=request.GET.get('classTime'),
                                         assignedTeacher_Fk=request.GET.get('assignedTeacher')):
            return HttpResponse("You have already select another class at the same time")
        else:
            classRoutine = ClassRoutine()
            assignedTeacherId = CourseAssignTeacher.objects.filter(
                emp_Id_Fk__emp_shortForm=request.session['username'],
                courseAssignTeacher_course_Id_Fk=request.GET.get(
                    'course'))
            for i in assignedTeacherId:
                teacherId = i.courseAssignTeacher_Id
            classRoutine.assignedTeacher_Fk_id = teacherId
            classRoutine.course_Id_Fk_id = request.GET.get('course')
            classRoutine.classTime_Id_Fk_id = request.GET.get('classTime')
            classRoutine.classRoom_Id_Fk_id = request.GET.get('room')
            classRoutine.dayOfWeek = request.GET.get('days')
            classRoutine.semesterTry = semester
            classRoutine.teacher_Id = teacherMainId
            classRoutine.save()
            fullRoutine = ClassRoutine.objects.filter()
            # return render(request, 'classRoutine.html', {'fullRoutine': fullRoutine})
            return HttpResponse("Saved")
            # else:
            #     return HttpResponse("You are not allowed")

    else:
        assignedTeacherId = Employee.objects.filter(emp_shortForm=request.session['username'])
        for i in assignedTeacherId:
            teacherId = i.emp_priority

        if teacherId == 1 and PriorityHandling.objects.filter(emp_teacher_Id_Fk__emp_priority=teacherId,
                                                              priority_status="active"):
            request.session['routine'] = 'visible'
            courseList = CourseAssignTeacher.objects.filter(
                emp_Id_Fk__emp_shortForm=request.session['username'])  # teacherId use korte hbe
            courseListToCompare = CourseAssignTeacher.objects.filter(
                emp_Id_Fk__emp_shortForm=request.session['username']).values_list(
                'courseAssignTeacher_course_Id_Fk')  # teacherId use korte hbe

            courseListTableCount = ClassRoutine.objects.filter(course_Id_Fk__in=courseListToCompare).values(
                'course_Id_Fk__course_code').annotate(the_count=Count('course_Id_Fk'))

            roomList = ClassRoom.objects.all()
            timeList = ClassTime.objects.all()
            fullRoutine = ClassRoutine.objects.filter()

            return render(request, 'classRoutineTry.html',
                          {'fullRoutine': fullRoutine, 'roomList': roomList, 'timeList': timeList,
                           'courseList': courseList,
                           'courseListTableCount': courseListTableCount})

        elif PriorityHandling.objects.filter(emp_teacher_Id_Fk__emp_priority=teacherId - 1, priority_status="deactive"):
            if PriorityHandling.objects.filter(emp_teacher_Id_Fk__emp_priority=teacherId, priority_status="active"):
                request.session['routine'] = 'visible'
                # teacherList = CourseAssignTeacher.objects.all()

                # courseList = CourseAssignTeacher.objects.all()

                courseList = CourseAssignTeacher.objects.filter(
                    emp_Id_Fk__emp_shortForm=request.session['username'])  # teacherId use korte hbe
                courseListToCompare = CourseAssignTeacher.objects.filter(
                    emp_Id_Fk__emp_shortForm=request.session['username']).values_list(
                    'courseAssignTeacher_course_Id_Fk')  # teacherId use korte hbe

                courseListTableCount = ClassRoutine.objects.filter(course_Id_Fk__in=courseListToCompare).values(
                    'course_Id_Fk__course_code').annotate(the_count=Count('course_Id_Fk'))

                roomList = ClassRoom.objects.all()
                timeList = ClassTime.objects.all()
                fullRoutine = ClassRoutine.objects.filter()
                # return render(request, 'classRoutine.html',
                #               {'fullRoutine': fullRoutine, 'roomList': roomList, 'timeList': timeList,
                #                'teacherList': teacherList, 'courseList': courseList})
                return render(request, 'classRoutineTry.html',
                              {'fullRoutine': fullRoutine, 'roomList': roomList, 'timeList': timeList,
                               'courseList': courseList,
                               'courseListTableCount': courseListTableCount})
            else:
                request.session['routine'] = "not visible"
                fullRoutine = ClassRoutine.objects.filter()
                editingTurn = PriorityHandling.objects.all()
                for ed in editingTurn:
                    e = ed.emp_teacher_Id_Fk.emp_shortForm
                return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine, 'editingTurn': e})
        else:
            request.session['routine'] = "not visible"
            fullRoutine = ClassRoutine.objects.filter()
            editingTurn = PriorityHandling.objects.all()
            for ed in editingTurn:
                e = ed.emp_teacher_Id_Fk.emp_shortForm
            return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine, 'editingTurn': e})


def classRoutineFullView_view(request):
    fullRoutine = ClassRoutine.objects.all()
    request.session['routine'] = "not visible"
    return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine})


def classRoutineBySyllabus_view(request):
    fullRoutine = ClassRoutine.objects.filter(course_Id_Fk__syl_Id=request.GET.get("syl"))  # get routine by syllabus id
    return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine})


def classRoutineByCourse_view(request):
    fullRoutine = ClassRoutine.objects.filter(
        course_Id_Fk=request.GET.get("course"))  # get routine by course id/course code
    return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine})


def classRoutineByCourseList_view(request):
    courseList = Course.objects.filter(syl_Id=2).values_list("id")
    fullRoutine = ClassRoutine.objects.filter(course_Id_Fk__in=courseList)  # get routine by list of course
    return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine})


def classRoutineByYear(request):
    # results = []
    # courseList = Course.objects.all()
    # for a in courseList:
    #     if a.course_code[4] == request.GET.get("year"):
    #         results.append(a.id)
    # fullRoutine = ClassRoutine.objects.filter(course_Id_Fk__in=results)  # get routine by year/4th year
    # return render(request, 'classRoutine.html', {'fullRoutine': fullRoutine})

    courseList = Course.objects.filter(semester_Id=request.GET.get("semester"))
    fullRoutine = ClassRoutine.objects.filter(
        course_Id_Fk__in=courseList)  # get routine by year/4th year  http://127.0.0.1:8000/routine/routineByYear/?semester=1
    return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine})


def classRoutineByTeacher_view(request):
    assignedTeacherId = Employee.objects.filter(emp_shortForm=request.session['username'])
    for i in assignedTeacherId:
        teacherMainId = i.emp_Id
    fullRoutine = ClassRoutine.objects.filter(teacher_Id=teacherMainId)  # get routine by list of course
    return render(request, 'classRoutineTry.html', {'fullRoutine': fullRoutine})
    return


# def index(request):
#     results = []
#     if request.GET.get("sid"):
#         sid = request.GET.get("sid")
#         all = Syllabus.objects.all()
#         # results = all
#         for a in all:
#             if (a.coures_code[4] == sid):
#                 results.append({'coures_code': a.coures_code,
#                                 'course_title': a.course_title,
#                                 'course_credit': a.course_credit})
#
#         return render(request, 'ViewAll.html', {'results': results})
#
#     else:
#         return render(request, 'ViewAll.html')


def onLoadCompare(day, time):
    count = 0
    if ClassRoutine.objects.filter(dayOfWeek=day, classTime_Id_Fk=time):
        count = 1
        return count
    return count


def passToNextTeacher(request):
    # another teacher data entry part
    assignedTeacherId = Employee.objects.filter(emp_shortForm=request.session['username'])
    for i in assignedTeacherId:
        teacherPriority = i.emp_priority
    another = Employee.objects.filter(emp_priority=teacherPriority + 1)
    if another:
        for a in another:
            anotherTeacherId = a.emp_Id
        priorityHandling = PriorityHandling()
        priorityHandling.emp_teacher_Id_Fk_id = anotherTeacherId
        priorityHandling.priority_start = datetime.now()
        priorityHandling.priority_end = datetime.now() + timedelta(hours=12)
        priorityHandling.priority_status = 'active'
        priorityHandling.save()
        request.session['routine'] = "not visible"

    # login teacher data update part
    obj = PriorityHandling.objects.get(emp_teacher_Id_Fk__emp_shortForm=request.session['username'])
    obj.priority_status = "deactive"
    obj.save()
    return HttpResponse("Done")


def createPdf_view(request):
    width, height = A4
    styles = getSampleStyleSheet()
    styleN = styles["BodyText"]
    styleN.alignment = TA_LEFT
    styleBH = styles["Normal"]
    styleBH.alignment = TA_CENTER

    courseList = Course.objects.filter(semester_Id=request.GET.get("semester"))
    fullRoutine = ClassRoutine.objects.filter(course_Id_Fk__in=courseList)  # get routine by year/4th year

    sat1var = "-"
    sat2var = "-"
    sat3var = "-"
    sat4var = "-"
    sun1var = "-"
    sun2var = "-"
    sun3var = "-"
    sun4var = "-"
    mon1var = "-"
    mon2var = "-"
    mon3var = "-"
    mon4var = "-"
    tue1var = "-"
    tue2var = "-"
    tue3var = "-"
    tue4var = "-"
    wed1var = "-"
    wed2var = "-"
    wed3var = "-"
    wed4var = "-"
    thu1var = "-"
    thu2var = "-"
    thu3var = "-"
    thu4var = "-"
    fri1var = "-"
    fri2var = "-"
    fri3var = "-"
    fri4var = "-"

    for foo in fullRoutine:
        if foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Sat':
            sat1var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 2 and foo.dayOfWeek == 'Sat':
            sat2var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 3 and foo.dayOfWeek == 'Sat':
            sat3var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 4 and foo.dayOfWeek == 'Sat':
            sat4var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Sun':
            sun1var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 2 and foo.dayOfWeek == 'Sun':
            sun2var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 3 and foo.dayOfWeek == 'Sun':
            sun3var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 4 and foo.dayOfWeek == 'Sun':
            sun4var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Mon':
            mon1var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 2 and foo.dayOfWeek == 'Mon':
            mon2var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 3 and foo.dayOfWeek == 'Mon':
            mon3var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 4 and foo.dayOfWeek == 'Mon':
            mon4var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Tues':
            tue1var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 2 and foo.dayOfWeek == 'Tues':
            tue2var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 3 and foo.dayOfWeek == 'Tues':
            tue3var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 4 and foo.dayOfWeek == 'Tues':
            tue4var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Wed':
            wed1var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 2 and foo.dayOfWeek == 'Wed':
            wed2var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 3 and foo.dayOfWeek == 'Wed':
            wed3var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 4 and foo.dayOfWeek == 'Wed':
            wed4var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Thurs':
            thu1var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 2 and foo.dayOfWeek == 'Thurs':
            thu2var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 3 and foo.dayOfWeek == 'Thurs':
            thu3var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 4 and foo.dayOfWeek == 'Thurs':
            thu4var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 1 and foo.dayOfWeek == 'Fri':
            fri1var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 2 and foo.dayOfWeek == 'Fri':
            fri2var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 3 and foo.dayOfWeek == 'Fri':
            fri3var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number
        elif foo.classTime_Id_Fk_id == 4 and foo.dayOfWeek == 'Fri':
            fri4var = foo.course_Id_Fk.course_code + "\n" + foo.assignedTeacher_Fk.emp_Id_Fk.emp_shortForm + "\n room:" + foo.classRoom_Id_Fk.room_number

    def coord(x, y, unit=1):
        x, y = x * unit, height - y * unit
        return x, y

    # Headers
    day = Paragraph('''&nbsp''', styleBH)
    nineToTen = Paragraph('''<b>9.00-10.20</b>''', styleBH)
    tenToEleven = Paragraph('''<b>10.20-11.25</b>''', styleBH)
    elevenTo12 = Paragraph('''<b>11.25-1.00</b>''', styleBH)
    twelveTo13 = Paragraph('''<b>2.00-4.00</b>''', styleBH)

    # Texts

    satDay = Paragraph('Saturday', styleN)
    sat1 = Paragraph(sat1var, styleN)
    sat2 = Paragraph(sat2var, styleN)
    sat3 = Paragraph(sat3var, styleN)
    sat4 = Paragraph(sat4var, styleN)

    # Texts
    sunDay = Paragraph('Sunday', styleN)
    sun1 = Paragraph(sun1var, styleN)
    sun2 = Paragraph(sun2var, styleN)
    sun3 = Paragraph(sun3var, styleN)
    sun4 = Paragraph(sun4var, styleN)

    # Texts
    monDay = Paragraph('Monday', styleN)
    mon1 = Paragraph(mon1var, styleN)
    mon2 = Paragraph(mon2var, styleN)
    mon3 = Paragraph(mon3var, styleN)
    mon4 = Paragraph(mon4var, styleN)

    # Texts
    tueDay = Paragraph('Tuesday', styleN)
    tue1 = Paragraph(tue1var, styleN)
    tue2 = Paragraph(tue2var, styleN)
    tue3 = Paragraph(tue3var, styleN)
    tue4 = Paragraph(tue4var, styleN)

    # Texts
    wedDay = Paragraph('Wednesday', styleN)
    wed1 = Paragraph(wed1var, styleN)
    wed2 = Paragraph(wed2var, styleN)
    wed3 = Paragraph(wed3var, styleN)
    wed4 = Paragraph(wed4var, styleN)

    # Texts
    thuDay = Paragraph('Thursday', styleN)
    thu1 = Paragraph(thu1var, styleN)
    thu2 = Paragraph(thu2var, styleN)
    thu3 = Paragraph(thu3var, styleN)
    thu4 = Paragraph(thu4var, styleN)

    # Texts
    friDay = Paragraph('Thursday', styleN)
    fri1 = Paragraph(fri1var, styleN)
    fri2 = Paragraph(fri2var, styleN)
    fri3 = Paragraph(fri3var, styleN)
    fri4 = Paragraph(fri4var, styleN)

    data = [[day, nineToTen, tenToEleven, elevenTo12, twelveTo13],
            [satDay, sat1, sat2, sat3, sat4],
            [sunDay, sun1, sun2, sun3, sun4],
            [monDay, mon1, mon2, mon3, mon4],
            [tueDay, tue1, tue2, tue3, tue4],
            [wedDay, wed1, wed2, wed3, wed4],
            [thuDay, thu1, thu2, thu3, thu4],
            [friDay, fri1, fri2, fri3, fri4]
            ]

    table = Table(data, colWidths=[2.05 * cm, 2.7 * cm, 5 * cm,
                                   3 * cm, 3 * cm])

    table.setStyle(TableStyle([
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))

    c = canvas.Canvas("a.pdf", pagesize=A4)
    table.wrapOn(c, width, height)
    table.drawOn(c, *coord(1.8, 9.6, cm))
    c.save()
    return HttpResponse("Done")
