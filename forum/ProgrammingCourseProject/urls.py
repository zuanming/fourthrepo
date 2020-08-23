from django.contrib import admin
from django.urls import path, include
import courses.views, reviews.views, forum.views, cart.views, checkout.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', courses.views.index, name='index'),
    path('unauthorised/', courses.views.unauthorised, name='unauthorised'),
    path('courses/', include('courses.urls')),
    path('reviews/', include('reviews.urls')),
    path('forum/', include('forum.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
]
