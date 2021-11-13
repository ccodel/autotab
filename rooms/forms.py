from django import forms

from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['building', 'room_number', 'display_name']
