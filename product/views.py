from django.shortcuts import render
from .models import Item, Category
from .filters import ItemFilter

def list(request):
    mainFilter = ItemFilter(request.GET, queryset=Item.objects.all())
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'items': items,
        'filter_main': mainFilter
    }
    return render(request, 'catalog.html' , context)

def byName(request, slug):
    item = Item.objects.get(slug=slug)
    context = {
        'item': item
    }
    return render(request, 'item_page.html' , context)

def byCategory(request, slug):
    filtered = Item.objects.filter(category__slug=slug)
    context = {
        'item': filtered,
        'category': slug
    }
    return render(request, 'category_page.html' , context)
