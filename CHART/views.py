# Create your views here.
from lib2to3.fixes.fix_input import context
from django.core.context_processors import request
from django.shortcuts import render, render_to_response
from django.template import Template , Context, RequestContext


def my_view(request):
    return render(request,'index.html')