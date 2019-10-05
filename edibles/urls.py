from django.urls import path

from edibles import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
]
