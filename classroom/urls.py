from django.urls import path
from classroom import views


urlpatterns= [
    path('',views.index)
]