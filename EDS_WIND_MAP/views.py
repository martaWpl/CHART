# Create your views here.
from django.shortcuts import render, render_to_response
from EDS_WIND_MAP import interface


def map(request):
    pogoda = interface.create_cities()
    #weather = interface.rendering(cities)
    content = {
        'cities': pogoda,
        #'weather': weather,
    }

    return render_to_response("tekst.html", content)
