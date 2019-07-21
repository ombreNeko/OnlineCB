from django.shortcuts import render
from classroom import models

# Create your views here.

def index(request):
    
    courses = models.Course.objects.all()

    context={
        "recommended_courses":courses
    }
    return render(request,'classroom/index.html',context)