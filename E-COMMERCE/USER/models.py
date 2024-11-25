from django.db import models
from django.contrib.auth.models import User
from PRODUCT.models import Laptop, PackageBundle



class Basket(models.Model):
    basket_id = models.BigAutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='OWNER', null=True)




    def __str__(self) -> str:
        return f'{self.user_id}"s Basket'



class BasketItems(models.Model):
    baskteItem_id = models.BigAutoField(primary_key=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='BASKET_MAIN')
    basket_laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE, related_name='LAPTOP_ITEMS', blank=True, null=True)
    basket_package = models.ForeignKey(PackageBundle, on_delete=models.CASCADE, related_name='PACKAGE_ITEMS', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.basket}'s Item"