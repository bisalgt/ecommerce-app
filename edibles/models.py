from django.db import models




class Season(models.Model):
    season_name = models.CharField(max_length=50)

    def __str__(self):
        return self.season_name



class Month(models.Model):
    month_name = models.CharField(max_length=50)
    inside_season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.month_name



class Fruit(models.Model):
    fruit_name = models.CharField(max_length=200)
    available_month = models.ManyToManyField(Month)

    def __str__(self):
        return self.fruit_name
    
    