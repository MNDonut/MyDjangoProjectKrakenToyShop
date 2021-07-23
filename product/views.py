from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Favorite, Item, Category
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
    if request.user.is_authenticated:
        isFavorite = Favorite.objects.filter(user=request.user, item=item)
        context = {
            'item': item,
            'isFavorite': isFavorite
        }
    return render(request, 'item_page.html' , context)

def byCategory(request, slug):
    filtered = Item.objects.filter(category__slug=slug)
    context = {
        'item': filtered,
        'category': slug
    }
    return render(request, 'category_page.html' , context)

def addFavorite(request, slug):
    item = Item.objects.get(slug=slug)
    isFavorite = Favorite.objects.filter(user=request.user, item=item)
    if isFavorite:
        isFavorite.delete()
        return redirect(f"/products/product/{slug}") 
    favorite = Favorite.objects.create(user=request.user, item=item)
    favorite.save()
    return redirect(f"/products/product/{slug}")   