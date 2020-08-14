from django.shortcuts import render, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from courses.models import Course
from django.contrib.auth.decorators import login_required, permission_required
import datetime

def index(request):
    questions = Question.objects.all()
    return render(request, 'forum/index.template.html', {
        'questions':questions
    })


def create_question(request):
    if request.method=="POST":
        question_form = QuestionForm(request.POST)
        question = question_form.save(commit=False)
        question.user = request.user
        question.course = get_object_or_404(Course, pk=course_id)
        question.datetime = datetime.dateime.now()
        if question_form.is_valid():
            question_form.save()
            return redirect('view_forum')
    else:
        question_form = QuestionForm()
        return render(request, "forum/create_question.template.html", {
            'question_form':question_form
        })

