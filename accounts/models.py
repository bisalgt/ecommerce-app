from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user_name = models.OneToOneField(User, verbose_name="username", on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=17, null=True, blank=True)

    # def __str__(self):
    #     # return self.user_name.email
    #     return self.user_name.username
    
