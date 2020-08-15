from django.shortcuts import render, reverse, HttpResponse, get_object_or_404
from django.conf import settings
import stripe
from courses.models import Course
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def checkout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('shopping_cart', {})

    line_items = []
    all_course_ids = []

    for course_id, course in cart.items():
        course_model = get_object_or_404(Course, pk=course_id)

        item = {
            "name": course_model.title,
            "amount": int(course_model.cost * 100),
            "quantity": course['qty'],
            "currency": "usd",

        }

        line_items.append(item)
        all_course_ids.append(str(book_model.id))

    current_site = Site.objects.get_current()
    domain = current_site.domain

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        client_reference_id=request.user.id,
        metadata={
            "all_course_ids": ",".join(all_course_ids)
        },
        mode="payment",
        success_url=domain + reverse("checkout_success"),
        cancel_url=domain + reverse("checkout_cancelled")
    )


def checkout_cancelled(request):
    messages.success(request, f"Payment Cancelled!")
    return redirect('view_courses')


def checkout_success(request):
    messages.success(request, f"Payment Completed!")
    return redirect('view_courses')


@csrf_exempt
def payment_completed(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    return HttpResponse(status=400)

  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    handle_payment(session)

  return HttpResponse(status=200)
