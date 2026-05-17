from django.contrib import admin
from .models import Student,ImageModel

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name', 'age', 'created_at', 'updated_at')

admin.site.register(Student, StudentAdmin)

admin.site.register(ImageModel)
