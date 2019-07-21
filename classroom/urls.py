from django.urls import path
from classroom import views


urlpatterns= [
    path('',views.index),
    path('courses/',views.AllCourses),
    path('courses/<int:id>',views.course,name="get_course")
]