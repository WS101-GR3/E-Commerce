from django.db import models

# imports model from different application
from STORE.models import Store


# Create your models here.

class Parts(models.Model):
    category = [
        ('Motherboard','Motherboard'),
        ('CPU','CPU'),
        ('Storage','Storage'),
        ('Memory','Memory'),
        ('Power Supply Unit', 'Power Supply Unit'),
        ('CPU Cooler', 'CPU Cooler'),
        ('Graphics Card','Graphics Card'),
        ('Case','Case')
    ]

    parts_id = models.BigAutoField(null=False, primary_key=True)
    parts_store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None)
    parts_category = models.CharField(max_length=200, choices=category, default=category[0])
    parts_name = models.CharField(max_length=200)
    parts_description = models.TextField()
    parts_img = models.ImageField(default='Desert.jpg')
    parts_price = models.BigIntegerField()
    parts_quantity = models.BigIntegerField()
    parts_rate = models.BigIntegerField(default=0)
    isSoldOut = models.BooleanField(default=False)



    def __str__(self) -> str:
        return self.parts_name


class PackageBundle(models.Model):
    category = [
        ('PreBuild','PreBuild'),
        ('UserBuild','UserBuild')
    ]


    unit_id = models.BigAutoField(null=False, primary_key=True)
    bundle_category = models.CharField(max_length=100, choices=category, default=category[0])
    bundle_banner = models.ImageField(default='Desert.jpg')
    bundle_name = models.CharField(max_length=200)
    motherboard_unit = models.ForeignKey(Parts, on_delete=models.CASCADE, default=None, related_name='bundle_motherboard')
    processor_unit= models.ForeignKey(Parts, on_delete=models.CASCADE, default=None, related_name='bundle_processor')
    storage_unit = models.ForeignKey(Parts, on_delete=models.CASCADE, default=None,related_name='bundle_storage')
    memory_unit= models.ForeignKey(Parts, on_delete=models.CASCADE, default=None, related_name='bundle_memory')

    # PERIPHERALS
    PSU_unit = models.ForeignKey(Parts, on_delete=models.CASCADE, default=None, related_name='bundle_PSU')
    CPU_cooler_unit = models.ForeignKey(Parts, on_delete=models.CASCADE, default=None, related_name='bundle_CPU_COOLER')
    GPU_unit = models.ForeignKey(Parts, on_delete=models.CASCADE, default=None, related_name='bundle_GPU')
    case_unit = models.ForeignKey(Parts, on_delete=models.CASCADE, default=None, related_name='bundle_case')

    bundle_total_price = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.bundle_name


class Laptop(models.Model):
    lap_id = models.AutoField(primary_key=True)
    banner = models.ImageField(default='Hydrangeas.jpg')


    name = models.CharField(max_length=100)

    processor = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    graphic_card = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)
    keyboard = models.CharField(max_length=100)
    wifi = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.BigIntegerField(default=150)



class Review(models.Model):
    review_id = models.BigAutoField(null=False, primary_key=True)
    product_topic = models.ForeignKey(Parts, on_delete=models.CASCADE, default=None)
    # review_author
    review_context = models.TextField()


    def __str__(self) -> str:
        return self.review_context