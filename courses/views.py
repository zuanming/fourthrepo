from django.shortcuts import render, HttpResponse

# View Functions

def index(request):
    return HttpResponse("Home")


def view_courses(request):
    return render(request, "courses/view_courses.template.html")

