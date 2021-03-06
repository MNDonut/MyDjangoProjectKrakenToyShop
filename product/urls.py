from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.list, name='catalog'),
    path('favorite/', views.favorite, name='favorite'),
    path('category/<slug:slug>/', views.byCategory , name='byCategory'),
    path('product/<slug:slug>/', views.byName, name='byName'),
    path('product/addFavorite/<slug:slug>', views.addFavorite, name='addFavorite'),
    path('product/removeFavorite/<slug:slug>', views.removeFavorite, name='removeFavorite'),
    path('comparison/', views.comparison, name='comparison'),
    path('product/addToCompare/<slug:slug>', views.addToCompare, name='addToCompare'),
    path('product/removeCompare/<slug:slug>', views.removeCompareItem, name='removeCompareItem'),

]