from django.shortcuts import render, get_object_or_404, reverse, redirect
from courses.models import Course
from django.contrib import messages


def add_to_cart(request, course_id):
    cart = request.session.get('shopping_cart', {})

    if course_id not in cart:
        course = get_object_or_404(Course, pk=course_id)
        cart[course_id] = {
            'id': course_id,
            'title': course.title,
            'cost': float(course.cost),
            'qty': 1,
        }
    else:
        cart[course_id]['qty'] += 1
    request.session['shopping_cart'] = cart
    messages.success(request, f"'{cart[course_id]['title']}' added to cart!")
    return redirect(reverse('view_courses'))


def view_cart(request):
    cart = request.session.get('shopping_cart', {})

    return render(request, 'cart/view_cart.template.html', {
        'cart': cart
    })


def remove_from_cart(request, course_id):
    cart = request.session.get('shopping_cart',{})
    item_name = cart[course_id]['title']
    if course_id in cart:
        del cart[course_id]
        request.session['shopping_cart'] = cart
        messages.success(request, f"'{item_name}' course removed from cart!")
    return redirect(reverse('view_cart'))


def update_quantity(request, course_id):
    cart = request.session.get('shopping_cart')
    if course_id in cart:
        cart[course_id]['qty']= request.POST['qty']
        request.session['shopping_cart'] = cart
    messages.success(request, f"Cart quantity of '{cart[course_id]['title']}' updated!")
    return redirect(reverse('view_cart'))