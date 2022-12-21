from django.contrib import admin
from . models import Course,Contact,Staff
# Register your models here.
admin.site.register(Course)

class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,Customerdetails)

admin.site.register(Staff)
