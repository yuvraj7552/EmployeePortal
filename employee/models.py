from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    position = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)