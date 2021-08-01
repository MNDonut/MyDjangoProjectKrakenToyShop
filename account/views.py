from django.shortcuts import render, redirect
from .forms import RegistrationForm
from product.models import Category, Favorite, CompareItem, Item

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to page login with its context(form)
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    
    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def home(request):
    randomItems = Item.objects.all().order_by('?')[:5]
    favoriteItems = Favorite.objects.all()[:5]
    comparingItems = CompareItem.objects.all()[:5]
    categories = Category.objects.all()
    context = {
        'random': randomItems,
        'favorite': favoriteItems,
        'comparing': comparingItems,
        'categories': categories
    }
    return render(request, 'common/index.html', context)