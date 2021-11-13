from django.urls import path

from .views import *

urlpatterns = [
    path('', TeamListView.as_view(), name='team_list'),
    path('<uuid:pk>', TeamDetailView.as_view(), name='team'),
]
