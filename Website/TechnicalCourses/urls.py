from . import views
from django.urls import path , include

app_name = 'TechnicalCourses'
urlpatterns = [
    path('',views.Courses,name='Courses'),
    path('<int:course_id>/',views.detail,name='detail'),
    path('<int:course_id>/yourchoice/',views.yourchoice,name='yourchoice')
]