# Create your views here.
import json
from django.shortcuts import render, render_to_response
import sys
from EDS_WIND_MAP import interface


def map(request):
    miasta = interface.create_cities(40)
    pogoda =[]
    for one in miasta:

        try:
            pogoda.append(interface.rendering(one))
        except:
             print "Unexpected error:"
             raise



    content = {
        'cities': pogoda,
    }


    return render_to_response("tekst.html", content)
