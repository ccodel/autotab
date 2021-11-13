import uuid

from django.db import models
from django.urls import reverse

from rooms.models import *
from teams.models import *

class Pairing(models.Model):
    id = models.UUIDField(
          primary_key=True,
          default=uuid.uuid4,
          editable=False)
    round_num = models.IntegerField()
    prosecution = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE,
        related_name='prosecution',
    )
    defense = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE,
        related_name='defense',
    )
    room = models.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE,
    )

    ballot1_score = models.IntegerField(blank=True, null=True)
    ballot1_initials = models.CharField(max_length=2, blank=True, null=True)
    ballot2_score = models.IntegerField(blank=True, null=True)
    ballot2_initials = models.CharField(max_length=2, blank=True, null=True)

    def pros_str(self):
        return self.prosecution.display_name

    def def_str(self):
        return self.defense.display_name

    def get_absolute_url(self):
        return reverse('pairing', args=[str(self.id)])

    def rankings(self):
        return Ranking.objects.select_related().filter(pairing = self.id)

class Ranking(models.Model):

    pairing = models.ForeignKey(
        'rounds.Pairing',
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE
    )

    student = models.CharField(max_length=100)
    ranks = models.IntegerField()
