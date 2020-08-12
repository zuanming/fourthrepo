from django.contrib import admin
from django.urls import path, include
import courses.views

urlpatterns = [
    path('', courses.views.view_courses, name='view_courses'),
    path('tutors/', courses.views.view_tutors, name='view_tutors'),
    path('tutors/<tutor_id>', courses.views.view_tutor_details, name='view_tutor_details'),
    path('<course_id>', courses.views.view_course_details, name='view_course_details'),
]
