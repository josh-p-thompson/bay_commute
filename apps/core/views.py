from django.shortcuts import render
from . import bart

def etas(request):
    print('------ viewing ETAs')

    arrivals = bart.station_arrivals()
    stations = bart.station_dict()

    context = {
        'stations': stations,
    }
    return render(request, 'pages/logged_out.html', context)

def etas_lookup(request, stn_abbr):
    print('------ viewing ETAs')

    arrivals = bart.station_arrivals(stn_abbr=stn_abbr)
    stations = bart.station_dict()

    context = {
        'stops': arrivals,
        'stations': stations,
    }
    return render(request, 'pages/etas.html', context)