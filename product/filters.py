from django.db.models import fields
from django_filters import FilterSet
import django_filters
from django import forms
from .models import Color, Item, Age, Material, Country

class ItemFilter(FilterSet):
    price = django_filters.OrderingFilter(
        # model field name: parameter name
        fields=('price', 'price'),
        # change basic labels of the filter choices
        field_labels = {
            'price': 'From cheaper to expensive',
            '-price': 'From expensive to cheaper'
        },
        label='Order',
    )

    price_gte = django_filters.NumberFilter(field_name='price', label='Price from: ', lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price', label='Price to: ', lookup_expr='lte')

    color = django_filters.ModelMultipleChoiceFilter(queryset=Color.objects.all(), 
                                                     widget=forms.CheckboxSelectMultiple())
    material = django_filters.ModelMultipleChoiceFilter(queryset=Material.objects.all(), 
                                                        widget=forms.CheckboxSelectMultiple())
    age = django_filters.ModelMultipleChoiceFilter(queryset=Age.objects.all(), 
                                                   widget=forms.CheckboxSelectMultiple())
    country = django_filters.ModelMultipleChoiceFilter(queryset=Country.objects.all(), 
                                                      widget=forms.CheckboxSelectMultiple())
                                                      
    class Meta:
        model = Item
        fields = ["price_gte", "price_lte" , "price", "color", "material", "age", "country", "in_stock"]