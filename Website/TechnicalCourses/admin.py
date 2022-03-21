from django.contrib import admin

# Register your models here.
from .models import AllCourses , details

admin.site.register(AllCourses)
admin.site.register(details)