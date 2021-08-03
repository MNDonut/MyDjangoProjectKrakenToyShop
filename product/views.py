from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Favorite, Item, Category, CompareItem
from .filters import ItemFilter
from django.contrib.auth.decorators import login_required

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
    mainFilter = ItemFilter(request.GET, queryset=Item.objects.filter(category__slug=slug))
    filtered = Item.objects.filter(category__slug=slug)
    context = {
        'items': filtered,
        'category': slug,
        'filter': mainFilter
    }
    return render(request, 'category_page.html' , context)

@login_required
def addFavorite(request, slug):
    item = Item.objects.get(slug=slug)
    isFavorite = Favorite.objects.filter(user=request.user, item=item)
    if isFavorite:
        isFavorite.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))  
    favorite = Favorite.objects.create(user=request.user, item=item)
    favorite.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))  

@login_required
def removeFavorite(request, slug):
    item = Item.objects.get(slug=slug)
    favorite = Favorite.objects.get(item=item, user=request.user)
    favorite.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 

@login_required
def favorite(request):
    favoriteItems = Favorite.objects.filter(user=request.user)
    total = sum([favorite.item.price for favorite in favoriteItems])
    context = {
        'items': favoriteItems,
        'totalPrice': total
    }
    return render(request, 'favorite.html', context)

@login_required
def comparison(request):
    # zip two lists into one with pairs (item, isFavorite(bool)) to discover what heart to display)
    items = CompareItem.objects.filter(user=request.user)[:5]
    favoriteItems = Favorite.objects.filter(user=request.user)
    isFavoriteList = []
    for compareItem in items:
        for favoriteItem in favoriteItems:
            if compareItem.item == favoriteItem.item:
                isFavoriteList.append(True)
                break
        else:
            isFavoriteList.append(False)
    context = {
        'items': zip(items, isFavoriteList)
    }
    return render(request, 'comparison.html', context)

@login_required
def addToCompare(request, slug):
    item = Item.objects.get(slug=slug)
    isCompared = CompareItem.objects.filter(user=request.user, item=item)
    if isCompared:
        isCompared.delete()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))  
    compared = CompareItem.objects.create(user=request.user, item=item)
    compared.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))  

@login_required
def removeCompareItem(request, slug):
    item = Item.objects.get(slug=slug)
    compareItem = CompareItem.objects.get(item=item, user=request.user)
    compareItem.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER")) 