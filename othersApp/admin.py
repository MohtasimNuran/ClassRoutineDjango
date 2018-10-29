from django.contrib import admin
from othersApp.models import ClassTime, ClassRoom,Holiday

# Register your models here.

admin.site.register(Holiday)
admin.site.register(ClassTime)
admin.site.register(ClassRoom)