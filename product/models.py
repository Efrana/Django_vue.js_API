from django.db import models


# reate your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('pending', 'PENDING'),
        ('publish', 'PUBLISH'),
        ('stockout', 'STOCKOUT')

    )
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    price = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='PENDING')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photo', null=True)

    def __str__(self):
        return self.name