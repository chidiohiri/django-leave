from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)

    is_employee = models.BooleanField(default=True)
    is_hr = models.BooleanField(default=False)
    
    
