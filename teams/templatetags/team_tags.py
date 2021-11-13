from django import template
from django.db.models import Q

from rounds.models import *

register = template.Library()

@register.filter
def pairings(team, r):
    return Pairing.objects.filter(
        (Q(prosecution=team.id) | Q(defense=team.id)) & Q(round_num=r))

@register.filter
def record(team):
    return team.record()

@register.filter
def running_record(team):
    return team.running_record()

@register.filter
def pd(team):
    return team.pd()

@register.filter
def running_pd(team):
    return team.running_pd()

@register.filter
def cs(team):
    return team.cs()

@register.filter
def running_cs(team):
    return team.running_cs()

@register.filter
def total_ranks(ranking):
    rs = Ranking.objects.filter(student=ranking.student)
    s = 0
    for r in rs:
        s += r.ranks

    return s
