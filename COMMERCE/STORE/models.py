from django.db import models

# Create your models here.

class Store(models.Model):
    store_id = models.BigAutoField(null=False, primary_key=True)
    store_name = models.CharField(max_length=250, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # store_owner

    def __str__(self) -> str:
        return self.store_name