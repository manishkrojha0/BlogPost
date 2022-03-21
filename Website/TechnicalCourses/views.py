from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template import loader
from .models import AllCourses


# Create your views here.
def Courses(request):
    ac = AllCourses.objects.all()
    template = loader.get_template('TechnicalCourses/Courses.html')
    context = {
        'ac': ac
    }
    return HttpResponse(template.render(context, request))


def detail(request, course_id):
    # return HttpResponse("hiiiiii")
    # course = get_list_or_404(AllCourses, pk=course_id)
    course=AllCourses.objects.get(pk=course_id)
    return render(request, 'TechnicalCourses/detail.html',{
        'course':course
    })


# your choice

def yourchoice(request, course_id):
    course=AllCourses.objects.get(pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except(KeyError, AllCourses.DoesNotExist):
        return render(request, 'TechnicalCourses/detail.html', {
            'course': course,
            'error_message': "Select a valid option"
        })
    else:
        selected_ct.your_choice = True
        selected_ct.save()
        return render(request, 'TechnicalCourses/detail.html', {
            'course': course
        })
