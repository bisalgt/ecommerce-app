from django.db import models
from django.utils import timezone
from fruits.models import Fruits

class Seasons(models.Model):
    season_name = models.CharField(max_length=100)
    # season_months = models.ForeignKey(timezone.datetime.month, on_delete=models.CASCADE)
    fruits = models.ForeignKey(Fruits, on_delete=models.CASCADE)

    def __str__(self):
        return self.season_name