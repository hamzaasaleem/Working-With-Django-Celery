from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .task import *


# Create your views here.
def index(request):

    return HttpResponse("<h1>Hello</h1>")
