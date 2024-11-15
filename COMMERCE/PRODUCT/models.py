from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.BigIntegerField(null=False, primary_key=True)
    product_category = models.CharField(max_length=200) #todo: change it into a text field option
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_img = models.ImageField()
    product_price = models.BigIntegerField()
    product_quantity = models.BigIntegerField()
    isSoldOut = models.BooleanField(default=False)

    # Foreign Keys:
    # product_reviews
    # product_shop

    def __str__(self) -> str:
        return self.product_name