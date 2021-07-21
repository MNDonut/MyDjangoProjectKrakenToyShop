from django.db.models import fields
from django_filters import FilterSet
import django_filters
from .models import Item

class OrderFilter(FilterSet):
    sort_by_price = django_filters.OrderingFilter(
        # model field name: parameter name
        fields=('price', 'price'),
        # change basic labels of the filter choices
        field_labels = {
            'price': 'From cheaper to expensive',
            '-price': 'From expensive to cheaper'
        },
        label='Order',
        required=True
    )

    class Meta:
        model = Item
        fields = ""