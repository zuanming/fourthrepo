from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from .forms import ReviewForm
from courses.models import Course
import datetime

def index(request):
    reviews= Review.objects.all()
    return render(request, "reviews/index.template.html", {
        'reviews':reviews
    })


def create_review(request, course_id):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.user = request.user
        review.course = get_object_or_404(Course, pk=course_id)
        review.date = datetime.datetime.now()
        review.save()
        return redirect('view_course_details', course_id=review.course.id)
    else:
        form = ReviewForm()
