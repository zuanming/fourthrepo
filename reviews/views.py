from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Review
from .forms import ReviewForm, CommentForm
from courses.models import Course
import datetime

def index(request):
    reviews= Review.objects.all()
    return render(request, "reviews/index.template.html", {
        'reviews':reviews
    })


def create_review(request, course_id):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        review = review_form.save(commit=False)
        review.user = request.user
        review.course = get_object_or_404(Course, pk=course_id)
        review.datetime = datetime.datetime.now()
        if review_form.is_valid():
            review_form.save()
            return redirect('view_course_details', course_id=review.course.id)
        else:
            return redirect('view_course_details', course_id=review.course.id)
    else:
        review_form = ReviewForm()
        return review_form

def update_review(request, review_id):
    review_being_updated = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        update_review_form = ReviewForm(request.POST, instance=review_being_updated)
        if update_review_form.is_valid():
            update_review_form.save()
            return redirect('view_course_details', course_id=review_being_updated.course.id)
    else:
        update_review_form = ReviewForm(instance=review_being_updated)
        return render(request, 'reviews/update_review.template.html', {
            'form': update_review_form,
            'course':review_being_updated.course
        })


def delete_review(request, review_id):
    review_to_delete = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        review_to_delete.delete()
        return redirect('view_course_details', course_id=review_to_delete.course.id)
    else:
        return render(request, 'reviews/delete_review.template.html', {
            'review': review_to_delete
        })


def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.datetime = datetime.datetime.now()
            comment.user = request.user
            comment.save()
            return redirect('view_course_details', course_id=review.course.id)
    else:
        form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            'form': form,
            'review': review
        })