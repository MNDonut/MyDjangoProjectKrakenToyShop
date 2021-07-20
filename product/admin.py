from django.contrib import admin
from .models import Item, Color, Category, Age, Country, Material

admin.site.register(Item)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Age)
admin.site.register(Country)
admin.site.register(Material)