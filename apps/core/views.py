from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from apps.accounts.models import FavoriteStation
from django.contrib.auth.models import User

from . import bart

def home_logged_out(request):
    print('------ viewing Home (Logged Out)')

    if request.user.is_authenticated:
        return redirect('home_logged_in')

    stations = bart.station_dict()

    context = {
        'stations': stations,
    }
    return render(request, 'pages/home_logged_out.html', context)

@login_required
def home_logged_in(request):
    print('------ viewing Home (Logged In)')

    stations = bart.station_dict()
    favorite_stations = FavoriteStation.objects.filter(user=request.user).order_by('station')
    favorites = [station['station'] for station in favorite_stations.values()]
    arrivals = bart.station_arrivals()

    # schedules for favorited stations
    stops = {abbr: schedules for abbr, schedules in arrivals.items() if abbr in favorites}

    # dictionaries are unordered but going to order it anyway
    stops_ordered = {}
    for key in sorted(stops.keys()): 
        stops_ordered[key] = stops[key]

    context = {
        'stations': stations,
        'favorite_stations': favorite_stations,
        'stops': stops_ordered,
    }
    return render(request, 'pages/home_logged_in.html', context)

def station_lookup(request, stn_abbr):
    print('------ viewing Station Lookup')

    arrivals = bart.station_arrivals(stn_abbr=stn_abbr)
    stations = bart.station_dict()

    context = {
        'stops': arrivals,
        'stations': stations,
    }
    return render(request, 'pages/station_lookup.html', context)