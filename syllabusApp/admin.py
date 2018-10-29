from django.contrib import admin
from syllabusApp.models import Syllabus, Course, Level, Semester
from syllabusApp.forms import CourseForm
from django.shortcuts import render

from django.contrib.admin import AdminSite
# Register your models here.


admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Syllabus)
admin.site.register((Semester))


class MyAdminSite(AdminSite):
    def get_urls(self):
        from django.conf.urls import url
        urls = super(MyAdminSite, self).get_urls()
        urls += [
            url(r'^addCourse/$', self.admin_view(self.my_view))
        ]
        return urls

    # def my_view(self, request):
    #     return HttpResponse("Hello!")
    def my_view(self, request):
        if (request.POST.get('levelDrop')):
            form = CourseForm()
            level = request.POST.get('levelDrop')
            if (level == '1'):
                semesters = Semester.objects.filter(level_Id=level)
                return render(request, 'addCourse.html', {'semesters': semesters, 'form': form})
            elif (level == '2'):
                semesters = Semester.objects.filter(level_Id=level)
                return render(request, 'addCourse.html', {'semesters': semesters, 'form': form})
        else:
            form = CourseForm()
            return render(request, 'addCourse.html', {'form': form})


admin_site = MyAdminSite()