from django.urls import path
from django.views.generic import TemplateView

from accounts import views

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    # path('signup_generic/', views.UserSignUpCreateView.as_view(), name='signup-generic'),
    path('signup_success/', TemplateView.as_view(template_name ='accounts/signup_success.html'), name='signup-success'),
]
