from django.contrib import admin
from django.urls import path, include
import forum.views

urlpatterns = [
    path('', forum.views.index, name='view_forum'),
    path('create/', forum.views.create_question, name='create_question'),
    path('update/<question_id>', forum.views.update_question, name='update_question')
]
