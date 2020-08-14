from django.contrib import admin
from django.urls import path, include
import forum.views

urlpatterns = [
    path('', forum.views.index, name='view_forum'),
    path('question/create/', forum.views.create_question, name='create_question'),
    path('question/update/<question_id>', forum.views.update_question, name='update_question'),
    path('question/delete/<question_id>', forum.views.delete_question, name='delete_question'),
    path('answer/create/<question_id>', forum.views.create_answer, name='create_answer'),
    path('answer/update/<answer_id>', forum.views.update_answer, name='update_answer'),
    path('answer/delete/<answer_id>', forum.views.delete_answer, name='delete_answer'),
]
