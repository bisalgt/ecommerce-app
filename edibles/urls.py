from django.urls import path

from edibles import views

urlpatterns = [
    path('', views.home, name='home' ),
]
