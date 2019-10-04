from django.shortcuts import render

from edibles.models import Fruit, Season, Month


def home(request):
    fruit_objects = Fruit.objects.all()
    season_objects = Season.objects.all()
    month_objects = Month.objects.all()

    context = {'fruit_objects': fruit_objects, 'season_objects':season_objects, 'month_objects':month_objects}

    return render(request, 'home.html', context)
