from django.db import models

class Fruits(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField()
    
    def __str__(self):
        return self.name