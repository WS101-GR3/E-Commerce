from django.db import models

# Create your models here.

class Store(models.Model):
    store_id = models.BigAutoField(null=False, primary_key=True)
    store_name = models.CharField(max_length=250, unique=True)
    store_address = models.CharField(max_length=250)
    store_owner = models.CharField(max_length=250)
    store_email = models.CharField(max_length=250)
    store_banner = models.ImageField()
    store_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.store_name