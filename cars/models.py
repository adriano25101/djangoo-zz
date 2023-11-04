from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
