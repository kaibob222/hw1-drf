from django.contrib import admin

from .models import Course, Grade, Student


admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Student)
