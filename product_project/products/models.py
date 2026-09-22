from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    production_date = models.DateField()

    def __str__(self):
        return self.name