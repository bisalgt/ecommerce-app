from django import forms
from django.contrib.auth.models import User
from django.db import models

from accounts.models import Profile

class UserSignUpViewForm(forms.ModelForm):

    class Meta:
        model = User
        fields = "username",'first_name', 'last_name', 'email'

    
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('address', 'phone_number')
