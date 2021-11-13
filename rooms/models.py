import uuid

from django.db import models

class Room(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    building = models.CharField(max_length=100)
    room_number = models.IntegerField()
    display_name = models.CharField(max_length=100)

    def __str__(self):
        return self.display_name
