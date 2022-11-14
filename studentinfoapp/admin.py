from django.contrib import admin

# Register your models here.
from studentinfoapp.models import StudentInfo

class StudentInfoAdmin(admin.ModelAdmin):
    list_display=['rollNo','name','mobile','addr']

admin.site.register(StudentInfo,StudentInfoAdmin)
