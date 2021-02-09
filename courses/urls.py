from django.contrib import admin
from django.urls import path, include
from .views import CoursesList, CoursesDetail
from . import views
app_name = 'Discussion_forum'
urlpatterns = [

    path('<int:pk>/', CoursesDetail.as_view(), name='course_detail'),
    path('', CoursesList.as_view(), name='courses'),



]
