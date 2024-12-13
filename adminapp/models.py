from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=10, default=0)
    image = models.ImageField(upload_to='image/')

    def average_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            return round(reviews.aggregate(models.Avg('rating'))['rating__avg'], 2)
        return 0

    def __str__(self):
        return self.name
    


