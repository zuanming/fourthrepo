from django.shortcuts import render
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from courses.models import Course
import datetime

def index(request):
    questions = Question.objects.all()
    return render(request, 'forum/index.template.html', {
        'questions':questions
    })


