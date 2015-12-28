# Create your views here.
import json
from django.shortcuts import render, render_to_response
from EDS_WIND_MAP import interface


def map(request):
    miasta = interface.create_cities(3)
    pogoda =[]
    miasto = interface.rendering(miasta[1])
    #long = miasto['longitude']
    #lat = miasto['latitude']
    for one in miasta:
        pogoda.append(interface.rendering(one))

    #weather = interface.rendering(cities)
    content = {
        'cities': pogoda,
        'miasta':miasta,
        'long':miasto['longitude'],
        'lat':miasto['latitude'],
        'speed':miasto['speed'],
        'dir':miasto['direction'],
    }

    return render_to_response("tekst.html", content)
