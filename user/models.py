from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_hosteller = models.BooleanField(default=False)
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)
    wallet_amount = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=10,blank=True)