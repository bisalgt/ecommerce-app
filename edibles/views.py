from django.shortcuts import render
from django.views.generic import TemplateView

from edibles.models import Fruit, Season, Month


def home(request):
    fruit_objects = Fruit.objects.all()
    season_objects = Season.objects.all()
    month_objects = Month.objects.all()

    context = {'fruit_objects': fruit_objects, 'season_objects':season_objects, 'month_objects':month_objects}

    return render(request, 'home.html', context)


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fruit_objects"] = Fruit.objects.all()
        context["season_objects"] = Season.objects.all()
        context["month_objects"] = Month.objects.all()
        return context
    