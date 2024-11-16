from .models import Product
from django_filters import FilterSet


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['gt', 'lt'],
            'category': ['exact'],
            'active': ['exact'],
        }