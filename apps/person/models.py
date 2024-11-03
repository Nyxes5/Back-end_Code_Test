import uuid
from django.db import models


class Person(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="A unique identifier for each Person instance, generated automatically.",
    )
    name = models.CharField(
        max_length=255, help_text="The person's name. Must be unique."
    )
    age = models.PositiveIntegerField(
        help_text="The person's age in years, as a positive integer. Must be 18+."
    )

    def __str__(self):
        return self.name
