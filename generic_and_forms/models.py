from django.db import models

# Create your models here.
class Jacket(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Značka")
    color = models.CharField(max_length=50, verbose_name="Farba")

    def __str__(self):
        return f"{self.brand} ({self.color})"