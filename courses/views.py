from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .models import Course, Tutor, Devtype
from .forms import CourseForm, TutorForm
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages


def index(request):
    return render(request, 'courses/index.template.html')


def unauthorised(request):
    return render(request, 'unauthorised.template.html')


def view_courses(request):
    cart = request.session.get('shopping_cart', {})
    cart_items = [cart[course_id]['title'] for course_id in cart]
    courses = Course.objects.all()
    devtypes = Devtype.objects.all()
    purchased_courses = []
    return render(request, "courses/view_courses.template.html", {
        'courses': courses,
        'devtypes': devtypes,
        'cart_items':cart_items,
    })


def view_course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    review_form = ReviewForm()
    return render(request, "courses/view_course_details.template.html", {
        'course': course,
        'form': review_form,
    })


def create_course(request):
    if not request.user.groups.filter(name="Administrators").exists():
        return redirect(reverse(unauthorised))
    if request.method == "POST":
        create_course_form = CourseForm(request.POST)
        if create_course_form.is_valid():
            create_course_form.save()
            messages.success(request, f"Course Created!")
            return(redirect('view_courses'))
        else:
            return render(request, 'courses/create_course.template.html',{
                'create_course_form':create_course_form
            })
    else:
        create_course_form = CourseForm()
        return render(request, 'courses/create_course.template.html',{
                'create_course_form':create_course_form
            })


def update_course(request, course_id):
    if not request.user.groups.filter(name="Administrators").exists():
        return redirect(reverse(unauthorised))
    course_being_updated = get_object_or_404(Course, pk=course_id)

    if request.method == "POST":
        update_course_form = CourseForm(request.POST, instance=course_being_updated)
        if update_course_form.is_valid():
            update_course_form.save()
            messages.success(request, f"Course Updated!")
            return(redirect('view_courses'))
        else:
            return render(request, 'courses/update_course.template.html',{
                'update_course_form':update_course_form
            })
    else:
        update_course_form = CourseForm(instance=course_being_updated)
        return render(request, 'courses/update_course.template.html',{
                'update_course_form':update_course_form,
            })


def delete_course(request, course_id):
    if not request.user.groups.filter(name="Administrators").exists():
        return redirect(reverse(unauthorised))
    course = get_object_or_404(Course, pk=course_id)
    if request.method=="POST":
        course.delete()
        messages.success(request, f"Course Deleted!")
        return redirect('view_courses')
    else:
        return render(request, 'courses/delete_course.template.html')


def view_tutors(request):
    tutors = Tutor.objects.all()
    return render(request, "courses/view_tutors.template.html", {
        'tutors': tutors
    })


def create_tutor(request):
    if not request.user.groups.filter(name="Administrators").exists():
        return redirect(reverse(unauthorised))
    if request.method == "POST":
        create_tutor_form = TutorForm(request.POST)
        if create_tutor_form.is_valid():
            create_tutor_form.save()
            messages.success(request, f"Tutor Added!")
            return(redirect('view_tutors'))
        else:
            return render(request, 'courses/create_tutor.template.html', {
                'create_tutor_form':create_tutor_form
            })
    else:
        create_tutor_form = TutorForm()
        return render(request, 'courses/create_tutor.template.html', {
                'create_tutor_form':create_tutor_form
            })


def update_tutor(request, tutor_id):
    if not request.user.groups.filter(name="Administrators").exists():
        return redirect(reverse(unauthorised))
    tutor_being_updated = get_object_or_404(Tutor, pk=tutor_id)
    if request.method == "POST":
        update_tutor_form = TutorForm(request.POST, instance=tutor_being_updated)
        if update_tutor_form.is_valid():
            update_tutor_form.save()
            messages.success(request, f"Tutor Updated!")
            return(redirect('view_tutors'))
        else:
            return render(request, 'courses/update_tutor.template.html',{
                'update_tutor_form':update_tutor_form
            })
    else:
        update_tutor_form = TutorForm(instance=tutor_being_updated)
        return render(request, 'courses/update_tutor.template.html',{
                'update_tutor_form':update_tutor_form,
            })


def delete_tutor(request, tutor_id):
    if not request.user.groups.filter(name="Administrators").exists():
        return redirect(reverse(unauthorised))
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    if request.method=="POST":
        tutor.delete()
        messages.success(request, f"Tutor Deleted!")
        return redirect('view_tutors')
    else:
        return render(request, 'courses/delete_tutor.template.html')


def view_tutor_details(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    return render(request, "courses/view_tutor_details.template.html", {
        'tutor': tutor
    })