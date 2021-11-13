from django.urls import path

from .views import *

urlpatterns = [
  path('', RoundsView.as_view(), name='rounds'),
  path('/rankings', RankingsView.as_view(), name='rankings'),
  path('<uuid:pk>', PairingDetailView.as_view(), name='pairing'),
]
