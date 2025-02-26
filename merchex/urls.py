from django.conf.urls import handler404
from django.urls import path
from . import views

urlpatterns = [
    # ...existing code...
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    # ...existing code...
]

handler404 = 'merchex.views.custom_404_view'
