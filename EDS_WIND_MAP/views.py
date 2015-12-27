# Create your views here.
from django.shortcuts import render


def map(request):
    return render(request, "tekst.html")
