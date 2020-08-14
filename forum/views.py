from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from courses.models import Course
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.contrib import messages


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
        question.datetime = datetime.datetime.now()
        if question_form.is_valid():
            question_form.save()
            messages.success(request, f"New question posted!")
            return redirect('view_forum')
    else:
        question_form = QuestionForm()
        return render(request, "forum/create_question.template.html", {
            'question_form':question_form
        })

def update_question(request, question_id):
    question_being_updated = get_object_or_404(Question, pk=question_id)
    if request.method=="POST":
        update_question_form = QuestionForm(request.POST, instance = question_being_updated)
        if update_question_form.is_valid():
            question.user = request.user
            question.datetime = datetime.datetime.now()
            question_form.save()
            messages.success(request, f"New question posted!")
            return redirect('view_forum')
    else:
        update_question_form = QuestionForm(instance = question_being_updated)
        return render(request, "forum/update_question.template.html", {
            'update_question_form': update_question_form
        })
