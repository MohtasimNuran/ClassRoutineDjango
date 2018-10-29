"""ClassRoutineDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from classRoutineApp import views

urlpatterns = [
    url(r'^calculatedate/', views.calculateClassEndingDate_view),
    url(r'^routine/', views.classRoutine_view),
    url(r'^routineBySyllabus/', views.classRoutineBySyllabus_view),
    url(r'^routineByCourse/', views.classRoutineByCourse_view),
    url(r'^routineByCourseList/', views.classRoutineByCourseList_view),
    url(r'^routineByYear/', views.classRoutineByYear),
    url(r'^priorityNext/', views.passToNextTeacher),
    url(r'^pdf/', views.createPdf_view),
    url(r'^endClassList/', views.classEndingDateList_view),
    url(r'^myRoutine/', views.classRoutineByTeacher_view),
    url(r'^fullRoutine/', views.classRoutineFullView_view),
]
