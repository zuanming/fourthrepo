from django.shortcuts import render, HttpResponse
from .models import Course, Tutor

# View Functions

def index(request):
    return HttpResponse("Home")


def view_courses(request):
    courses = Course.objects.all()
    return render(request, "courses/view_courses.template.html", {
        'courses':courses
    })

