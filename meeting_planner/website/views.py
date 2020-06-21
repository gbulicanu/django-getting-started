from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to meeting planner!")


def date(request):
    return HttpResponse(f"This page was server at {datetime.now()}")


def about(request):
    return HttpResponse("I'm Gheorghe and I watch courses on Pluralsight!")
