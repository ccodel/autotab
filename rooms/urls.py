from django.urls import path

from .views import *

urlpatterns = [
    path('', RoomListView.as_view(), name='room_list'),
]
