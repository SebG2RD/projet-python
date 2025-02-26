from django.conf.urls import handler404
from django.urls import path
from . import views

handler404 = 'listings.views.custom_404_view'

urlpatterns = [
    path('email-sent/', views.email_sent, name='email-sent'),
    path('bands/add/', views.band_create, name='band-create'),
]
