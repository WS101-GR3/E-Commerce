from django.db import models
from django.contrib.auth.models import User
from PRODUCT.models import Laptop, PackageBundle



class Basket(models.Model):
    user_id = models.PositiveIntegerField()
    basket_item_id = models.PositiveIntegerField(default=0)
    basket_item_name = models.CharField(max_length=350)
    basket_item_price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.basket_item_name