from django.forms.models import model_to_dict
from django.shortcuts import redirect, render
from .models import Favorite, Item, Category, CompareItem
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
        isCompared = CompareItem.objects.filter(user=request.user, item=item)
        context = {
            'item': item,
            'isFavorite': isFavorite,
            'isCompared': isCompared
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

def removeFavorite(request, slug):
    item = Item.objects.get(slug=slug)
    favorite = Favorite.objects.get(item=item, user=request.user)
    favorite.delete()
    return redirect(f"/products/favorite")  

def favorite(request):
    favoriteItems = Favorite.objects.filter(user=request.user)
    total = sum([favorite.item.price for favorite in favoriteItems])
    context = {
        'items': favoriteItems,
        'totalPrice': total
    }
    return render(request, 'favorite.html', context)

def comparison(request):
    items = CompareItem.objects.filter(user=request.user)[:5]
    context = {
        'items': items
    }
    return render(request, 'comparison.html', context)

def addToCompare(request, slug):
    item = Item.objects.get(slug=slug)
    isCompared = CompareItem.objects.filter(user=request.user, item=item)
    if isCompared:
        isCompared.delete()
        return redirect(f"/products/product/{slug}") 
    compared = CompareItem.objects.create(user=request.user, item=item)
    compared.save()
    return redirect(f"/products/product/{slug}")