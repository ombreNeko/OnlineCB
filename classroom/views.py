from django.shortcuts import render
from classroom import models

# Create your views here.

def index(request):

    courses = models.Course.objects.filter(recommended = True)

    context={
        "recommended_courses":courses
    }
    return render(request,'classroom/index.html',context)


def course(request, id):
    
    course= models.Course.objects.get(id = id)
  
    context={
        "course" : course
    }
    return render(request,'classroom/course.html',context)

def AllCourses(request):
    courses= models.Course.objects.all()

    context = {
        "courses":courses
    }
    return render(request,'classroom/allcourses.html',context)