from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room


def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, "rooms/list.html", {"rooms": rooms})


def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "rooms/detail.html", {"room": room})

