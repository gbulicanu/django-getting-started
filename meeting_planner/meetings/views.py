from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'meetings/detail.html', {'meeting': meeting})


def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, 'meetings/rooms_list.html', {'rooms': rooms})


def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, 'meetings/room_detail.html', {'room': room})


def new(request):
    if request.method == 'POST':
        # form has been submitted, process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MeetingForm()
    return render(request, 'meetings/new.html', {'form': form})
