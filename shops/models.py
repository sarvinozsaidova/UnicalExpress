from django.db import models

class Shop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    imageUrl = models.URLField(max_length=200)

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    parents = models.ManyToManyField('self', symmetrical=False, blank=True)

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    price = models.FloatField()
    images = models.ImageField()
    active = models.BooleanField(default=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)