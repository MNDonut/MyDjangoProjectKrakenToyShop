from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.list, name='catalog'),
    path('category/<slug:slug>/', views.byCategory , name='byCategory'),
    path('product/<slug:slug>/', views.byName, name='byName'),
    path('product/addFavorite/<slug:slug>', views.addFavorite, name='addFavorite')
]