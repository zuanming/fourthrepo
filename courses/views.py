from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course, Tutor

# View Functions

def index(request):
    return HttpResponse("Home")


def view_courses(request):
    courses = Course.objects.all()
    return render(request, "courses/view_courses.template.html", {
        'courses':courses
    })


def view_tutors(request):
    tutors = Tutor.objects.all()
    return render(request, "courses/view_tutors.template.html", {
        'tutors':tutors
    })


def view_tutor_details(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    print(tutor)
    return render(request, "courses/view_tutor_details.template.html", {
        'tutor':tutor
    })
    