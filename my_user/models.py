from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=100, null=True, blank=True)
    homepage = models.URLField(null=True)
    age = models.IntegerField(null=True)


