from django import forms
from django.db.models import Q

from .models import *
from rooms.models import *
from teams.models import *

class PairingForm(forms.ModelForm):
    class Meta:
        model = Pairing
        fields = ['room', 'prosecution', 'defense', 'round_num']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.all()
        self.fields['prosecution'].queryset = Team.objects.all()
        self.fields['defense'].queryset = Team.objects.all()

class BallotForm(forms.Form):
    ballot1_score = forms.IntegerField()
    ballot1_initials = forms.CharField(max_length=2)
    ballot2_score = forms.IntegerField()
    ballot2_initials = forms.CharField(max_length=2)


class RankingsForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ['pairing', 'team', 'student', 'ranks']

    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs.get('initial') is not None:
            p = Pairing.objects.get(pk=kwargs.get('initial').get('pairing'))
            print(p)
            self.fields['team'].queryset = Team.objects.filter(pk=p.prosecution.id) | Team.objects.filter(pk=p.defense.id)
        
            self.fields['pairing'].widget = forms.HiddenInput()
    '''
