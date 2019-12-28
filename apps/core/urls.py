from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home_logged_out, name='home_logged_out'),
    path('home', views.home_logged_in, name='home_logged_in'),
    path('<stn_abbr>', views.station_lookup, name='station_lookup'),
]
