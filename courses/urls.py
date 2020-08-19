from django.contrib import admin
from django.urls import path, include
import courses.views

urlpatterns = [
    path('', courses.views.view_courses, name='view_courses'),
    path('details/<course_id>', courses.views.view_course_details, name='view_course_details'),
    path('create/', courses.views.create_course, name='create_course'),
    path('update/<course_id>', courses.views.update_course, name='update_course'),
    path('delete/<course_id>', courses.views.delete_course, name='delete_course'),
    path('tutors/', courses.views.view_tutors, name='view_tutors'),
    path('tutors/details/<tutor_id>', courses.views.view_tutor_details, name='view_tutor_details'),
    path('tutors/create/', courses.views.create_tutor, name='create_tutor'),
    path('tutors/update/<tutor_id>', courses.views.update_tutor, name='update_tutor'),
    path('tutors/delete/<tutor_id>', courses.views.delete_tutor, name='delete_tutor'),
]
