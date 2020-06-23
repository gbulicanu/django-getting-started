from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting, Room


def welcome(request):
    return render(request,
                  "website/welcome.html",
                  {"meetings": Meeting.objects.all(),
                   "rooms": Room.objects.all()})


def date(request):
    return HttpResponse(f"This page was server at {datetime.now()}")


def about(request):
    return HttpResponse("I'm Gheorghe and I watch courses on Pluralsight!")
