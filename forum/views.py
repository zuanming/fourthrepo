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


def delete_question(request, question_id):
    question_to_delete = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        question_to_delete.delete()
        messages.success(request, f"Question removed!")
        return redirect('view_forum')
    else:
        return render(request, 'forum/delete_question.template.html', {
            'question': question_to_delete
        })


def create_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method=="POST":
        answer_form = AnswerForm(request.POST)
        answer = answer_form.save(commit=False)
        answer.user = request.user
        answer.datetime = datetime.datetime.now()
        answer.question = question
        if answer_form.is_valid():
            answer_form.save()
            messages.success(request, f"New answer posted!")
            return redirect('view_forum')
    else:
        answer_form = AnswerForm()
        return render(request, "forum/create_answer.template.html", {
            'answer_form':answer_form,
            'question':question,
        })


def update_answer(request, answer_id):
    answer_being_updated = get_object_or_404(Answer, pk=answer_id)
    if request.method=="POST":
        update_answer_form = AnswerForm(request.POST, instance = answer_being_updated)
        if update_answer_form.is_valid():
            answer.user = request.user
            answer.datetime = datetime.datetime.now()
            answer.save()
            answer.success(request, f"Answer updated!")
            return redirect('view_forum')
    else:
        update_answer_form = AnswerForm(instance = question_being_updated)
        return render(request, "forum/update_answer.template.html", {
            'update_answer_form': update_answer_form
        })


def delete_answer(request, answer_id):
    answer_to_delete = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'POST':
        answer_to_delete.delete()
        messages.success(request, f"Answer removed!")
        return redirect('view_forum')
    else:
        return render(request, 'forum/delete_answer.template.html', {
            'answer': answer_to_delete
        })