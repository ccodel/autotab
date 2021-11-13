from django.contrib import admin
from .models import *

class PairingsAdmin(admin.ModelAdmin):
    list_display = ("round_num", "prosecution", "defense",
        "ballot1_score", "ballot1_initials",
        "ballot2_score", "ballot2_initials")

class RankingsAdmin(admin.ModelAdmin):
    list_display = ("team", "student", "ranks")

admin.site.register(Pairing, PairingsAdmin)
admin.site.register(Ranking, RankingsAdmin)

