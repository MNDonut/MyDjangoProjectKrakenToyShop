from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from slugger import AutoSlugField

def isPositivePriceValidator(price):
    if price <= 0:
        raise ValidationError("Price can't be less zero!")

class Item(models.Model):
    image = models.ImageField(upload_to='images/', default='0')
    title = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=7, decimal_places=2, validators=[isPositivePriceValidator])
    color = models.ForeignKey('Color', on_delete=CASCADE, default='')
    category = models.ForeignKey('Category', on_delete=CASCADE, default='')
    material = models.ForeignKey('Material', on_delete=CASCADE, default='')
    age = models.ForeignKey('Age', on_delete=CASCADE, default='')
    description = models.CharField(max_length=5000)
    in_stock = models.BooleanField(default=True)
    guarantee = models.ForeignKey('Guarantee', on_delete=CASCADE, null=True)
    country = models.ForeignKey('Country', on_delete=CASCADE, default='')
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

class Color(models.Model):
    color = models.CharField(max_length=32)

    def __str__(self):
        return self.color

class Category(models.Model):
    category = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from='category', default='')

    class Meta:
        ordering = ['category']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category

class Country(models.Model):
    country = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.country

class Age(models.Model):
    age = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'Ages'

    def __str__(self):
        return self.age

class Material(models.Model):
    material = models.CharField(max_length=32)

    def __str__(self):
        return self.material

class Guarantee(models.Model):
    guarantee = models.CharField(max_length=32)

    def __str__(self):
        return self.guarantee

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ForeignKey('Item', on_delete=CASCADE)

    def __str__(self):
        return str(self.item)

class CompareItem(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ForeignKey('Item', on_delete=CASCADE)

    def __str__(self):
        return str(self.item)