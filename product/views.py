from django.shortcuts import render
from .models import Item, Category

def list(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items
    }
    return render(request, 'catalog.html' , context)

def byName(request, slug):
    item = Item.objects.get(slug=slug)
    context = {
        'items': item
    }
    return render(request, 'item_page.html' , context)

def byCategory(request, slug):
    filtered = Item.objects.filter(category__slug=slug)
    context = {
        'items': filtered,
        'category': slug
    }
    return render(request, 'category_page.html' , context)
