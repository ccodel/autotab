from django import forms

from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['school_name', 'team_number', 'display_name']
