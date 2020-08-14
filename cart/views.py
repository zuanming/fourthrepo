from django.shortcuts import render, get_object_or_404, reverse, HttpResponse
from courses.models import Course

def add_to_cart(request, course_id):
    cart = request.session.get('shopping_cart', {})

    if course_id not in cart:
        course = get_object_or_404(Course, pk=course_id)
        cart[course_id] = {
            'id':course_id,
            'title': course.title,
            'cost': 10,
            'qty': 1,
        }
        #change cost to variable

        request.session['shopping_cart'] = cart
        return HttpResponse('Course Added')
    else:
        cart[course_id]['qty']+=1
        request.session['shopping_cart'] = cart
        return HttpResponse('Course qty updated')

