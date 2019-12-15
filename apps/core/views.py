from django.shortcuts import render
from . import bart

def etas(request):
    print('------ viewing ETAs')

    arrivals = bart.station_arrivals()
    context = {
        'stops': arrivals,
    }
    return render(request, 'pages/base_etas.html', context)

def etas_lookup(request, stn_abbr):
    print('------ viewing ETAs')

    arrivals = bart.station_arrivals(stn_abbr=stn_abbr)
    context = {
        'stops': arrivals,
    }
    return render(request, 'pages/base_etas.html', context)