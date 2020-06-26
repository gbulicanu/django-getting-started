from django.urls import path

from . import views


urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms', views.rooms_list, name='rooms-list'),
    path('rooms/<int:id>', views.room_detail, name='room-detail'),
    path('new', views.new, name='new-meeting'),
]
