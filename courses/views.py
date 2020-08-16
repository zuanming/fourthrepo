from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course, Tutor, Devtype
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return HttpResponse("Home")


def view_courses(request):
    courses = Course.objects.all()
    devtypes = Devtype.objects.all()
    return render(request, "courses/view_courses.template.html", {
        'courses': courses,
        'devtypes': devtypes,
    })


def view_course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    review_form = ReviewForm()
    return render(request, "courses/view_course_details.template.html", {
        'course': course,
        'form': review_form,
    })


def view_tutors(request):
    tutors = Tutor.objects.all()
    return render(request, "courses/view_tutors.template.html", {
        'tutors': tutors
    })


def view_tutor_details(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    return render(request, "courses/view_tutor_details.template.html", {
        'tutor': tutor
    })