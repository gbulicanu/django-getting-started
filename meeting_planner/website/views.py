from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting


def welcome(request):
    return render(request,
                  "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse(f"This page was server at {datetime.now()}")


def about(request):
    return HttpResponse("I'm Gheorghe and I watch courses on Pluralsight!")
