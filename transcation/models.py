from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.utils import timezone
from food.models import Item
from cart.models import Cart,CartItem
class Transcation(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(default=0)
    is_printed = models.BooleanField(default=False)
    def transcate(self,cart):
        cart.is_active = False
        cart.save()
    