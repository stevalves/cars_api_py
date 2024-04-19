from django.db import models


class Car(models.Model):

    brand = models.CharField(max_length=85)
    model = models.CharField(max_length=85)
    spec = models.CharField(max_length=255)
    year = models.PositiveSmallIntegerField()
    fuel = models.CharField(max_length=85)
    km = models.PositiveIntegerField()
    color = models.CharField(max_length=85)
    fipe = models.PositiveIntegerField()
    description = models.TextField(max_length=500, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

