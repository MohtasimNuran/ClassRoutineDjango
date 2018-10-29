from django.shortcuts import render, HttpResponse
from othersApp.forms import HolidayForm
from datetime import date, timedelta, datetime
from othersApp.models import Holiday, ClassRoom, ClassTime


# Create your views here.

# def addHoliday_view(request):
#     if request.GET:
#         form = HolidayForm(request.GET)
#         if form.is_valid:
#             holidayStart = datetime.strptime(form['holidayStart_date'].value(), '%Y-%m-%d')
#             holidayEnd = datetime.strptime(form['holidayEnd_date'].value(), '%Y-%m-%d')
#             if holidayStart <= holidayEnd:
#                 dayLeft = (holidayEnd - holidayStart) + timedelta(days=1)
#
#             obj = form.save(commit=False)
#             obj.holidayInDays = dayLeft.days
#             obj.save()
#
#             return HttpResponse("Saved")
#         else:
#             return HttpResponse("Form is not valid")
#     else:
#         form = HolidayForm
#         return render(request, 'addHoliday.html', {'form': form})


def addHoliday_view(request):
    if request.GET:
        holiday = Holiday()
        holiday.holidayStart_date = datetime.strptime(request.GET.get('startDate'), '%Y-%m-%d')
        holiday.holidayEnd_date = datetime.strptime(request.GET.get('endDate'), '%Y-%m-%d')
        if holiday.holidayStart_date <= holiday.holidayEnd_date:
            dayLeft = (holiday.holidayEnd_date - holiday.holidayStart_date) + timedelta(days=1)

            holiday.holidayInDays = dayLeft.days
            holiday.holiday_description = request.GET.get('description')
            holiday.save()
            return HttpResponse("Saved")
        else:
            return HttpResponse("Invalid Date")

    else:
        holidayList = Holiday.objects.all()
        return render(request, 'addHoliday.html', {'holidayList': holidayList})


def addRoom_view(request):
    if request.GET:
        classRoom = ClassRoom()
        classRoom.room_type = request.GET.get('type')
        classRoom.room_number = request.GET.get('roomNumber')
        if ClassRoom.objects.filter(room_type=classRoom.room_type, room_number=classRoom.room_number):
            return HttpResponse("Room Data Already Exists")
        else:
            classRoom.save()
            return HttpResponse("Saved")
    else:
        roomList = ClassRoom.objects.all()
        return render(request, 'addRoom.html', {'roomList': roomList})


def addClassTime_view(request):
    if request.GET:
        classTime = ClassTime()
        classTime.time_period = request.GET.get('time')
        if ClassTime.objects.filter(time_period=classTime.time_period):
            return HttpResponse("Already Exists")
        else:
            classTime.save()
            return HttpResponse("Save")
    else:
        timeList = ClassTime.objects.all()
        return render(request, 'addClassTime.html', {'timeList': timeList})
