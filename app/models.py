from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    PRODUCT = (
        ('pent','P' ),
        ( 'shirt','S'),
        ('track soot','T' ),
    )

    TAG = (
        ('recomened','R' ),
        ('offer','O' ),
        ('sale','S' ),
    )

    product = models.CharField(max_length=10, choices=PRODUCT)
    name = models.CharField(max_length=60)
    tag = models.CharField(max_length=15, choices=TAG)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    stock = models.IntegerField()

    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', '-create']

    def __str__(self):
        return str([self.name,self.product,self.tag,self.description])
