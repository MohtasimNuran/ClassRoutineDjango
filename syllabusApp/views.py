from django.shortcuts import render, HttpResponse
from syllabusApp.forms import CourseForm
from syllabusApp.models import Semester


# Create your views here.
# def addCourse_view(request):
#     form = CourseForm()
#     if (request.POST) and (form.is_valid):
#         if form.is_valid:
#             form.save()
#             return addCourse_view()
#         else:
#             return HttpResponse('form is not valid')
#     elif (request.POST.get('levelDrop')):
#         form = CourseForm()
#         level = request.POST.get('levelDrop')
#         if (level == '1'):
#             semesters = Semester.objects.filter(level_Id=level)
#             return render(request, 'addCourse.html', {'semesters': semesters, 'form': form})
#         elif (level == '2'):
#             semesters = Semester.objects.filter(level_Id=level)
#             return render(request, 'addCourse.html', {'semesters': semesters, 'form': form})
#     else:
#         form = CourseForm()
#         return render(request, 'addCourse.html', {'form': form})
def addCourse_view(request):
    if request.method == 'POST':
        form = CourseForm
        # post = CourseForm(request.POST.copy())
        # post.level_Id = request.session['Level']
        # request.POST = post

        # request.POST._mutable = True
        # request.POST['levelDrop'] = request.session['Level']

        # saveForm = CourseForm(request.POST)
        if CourseForm(request.POST).is_valid():
            CourseForm(request.POST).save()
            return HttpResponse('Saved')
        elif request.POST.get('levelDrop'):
            level = request.POST.get('levelDrop')
            request.session['Level'] = level
            if (level == '1'):
                semesters = Semester.objects.filter(level_Id=level)
                return render(request, 'addCourse.html', {'semesters': semesters, 'form': form})
            elif (level == '2'):
                semesters = Semester.objects.filter(level_Id=level)
                return render(request, 'addCourse.html', {'semesters': semesters, 'form': form})
        else:
            return HttpResponse('form is not valid')

    else:
        form = CourseForm
        return render(request, 'addCourse.html', {'form': form})
