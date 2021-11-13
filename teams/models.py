import uuid

from django.db import models
from django.urls import reverse
from django.db.models import Q

from rounds.models import *

class Team(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    school_name = models.CharField(max_length=100)
    team_number = models.IntegerField()
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name

    def get_absolute_url(self):
        return reverse('team', args=[str(self.id)])

    def pairings(self, r):
        return Pairing.objects.filter(
            (Q(prosecution=self.id) | Q(defense=self.id)) & Q(round_num=r))

    def record(self):
        r = [0, 0, 0, 0]

        for i in range(4):
            ps = list(self.pairings(i + 1))
            if ps is not None and len(ps) > 0:
                p = ps[0]
                if p.ballot1_score is None:
                    continue

                if p.prosecution.id == self.id:
                    if p.ballot1_score > 0:
                        r[i] += 1
                    elif p.ballot1_score == 0:
                        r[i] += 0.5

                    if p.ballot2_score > 0:
                        r[i] += 1
                    elif p.ballot2_score == 0:
                        r[i] += 0.5
                else:
                    if p.ballot1_score < 0:
                        r[i] += 1
                    elif p.ballot1_score == 0:
                        r[i] += 0.5

                    if p.ballot2_score < 0:
                        r[i] += 1
                    elif p.ballot2_score == 0:
                        r[i] += 0.5

        return r

    def running_record(self):
        r = self.record()
        rr = [0, 0, 0, 0]
        s = 0
        for i in range(4):
            s += r[i]
            rr[i] = s

        return rr

    def pd(self):
        d = [0, 0, 0, 0]

        for i in range(4):
            ps = list(self.pairings(i + 1))
            if ps is not None and len(ps) > 0:
                p = ps[0]
                if p.ballot1_score is None:
                    continue

                if p.prosecution.id == self.id:
                    d[i] += p.ballot1_score
                    d[i] += p.ballot2_score
                else:
                    d[i] -= p.ballot1_score
                    d[i] -= p.ballot2_score
        return d

    def running_pd(self):
        d = self.pd()
        dd = [0, 0, 0, 0]
        s = 0
        for i in range(4):
            s += d[i]
            dd[i] = s

        return dd

    def cs(self):
        c = [0, 0, 0, 0]

        for i in range(4):
            ps = list(self.pairings(i + 1))
            if ps is not None and len(ps) > 0:
                p = ps[0]
                if p.ballot1_score is None:
                    continue

                if p.prosecution.id == self.id:
                    c[i] += p.defense.record()[i]
                else:
                    c[i] += p.prosecution.record()[i]
        return c

    def running_cs(self):
        cc = [0, 0, 0, 0]
        c = self.cs()
        s = 0

        for i in range(4):
            s += c[i]
            cc[i] = s
        return cc
