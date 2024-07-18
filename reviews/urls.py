from django.urls import path
from . import views


urlpatterns = [
    path('', views.review, name='review'),
    path('thank-you', views.thank_you, name='thank-you'),
]
