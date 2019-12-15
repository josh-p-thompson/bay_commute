from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.etas, name='etas'),
]
