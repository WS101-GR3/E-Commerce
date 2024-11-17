from django.db import models

# Create your models here.

class Product(models.Model):
    category = [
        ('Laptop','Laptop'),
        ('Motherboard','Motherboard'),
        ('Processor','Processor'),
        ('Storage','Storage'),
        ('Memory','Memory')
    ]

    product_id = models.BigAutoField(null=False, primary_key=True)
    product_category = models.CharField(max_length=200, choices=category, default=category[0])
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_img = models.ImageField()
    product_price = models.BigIntegerField()
    product_quantity = models.BigIntegerField()
    product_rate = models.BigIntegerField(default=0)
    isSoldOut = models.BooleanField(default=False)

    # Foreign Keys:
    # product_reviews
    # product_shop

    def __str__(self) -> str:
        return self.product_name


class ProductBundle(models.Model):
    unit_id = models.BigAutoField(null=False, primary_key=True)
    bundle_name = models.CharField(max_length=200)
    motherboard_unit = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name='bundle_motherboard')
    processor_unit= models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name='bundle_processor')
    storage_unit = models.ForeignKey(Product, on_delete=models.CASCADE, default=None,related_name='bundle_storage')
    memory_unit= models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name='bundle_memory')

    def __str__(self) -> str:
        return self.bundle_name



class Review(models.Model):
    review_id = models.BigAutoField(null=False, primary_key=True)
    product_topic = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    # review_author
    review_context = models.TextField()


    def __str__(self) -> str:
        return self.review_context