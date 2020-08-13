from django.shortcuts import render
from .models import Review

def index(request):
    reviews= Review.objects.all()
    return render(request, "reviews/index.template.html", {
        'reviews':reviews
    })