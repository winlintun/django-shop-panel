from django_filters import FilterSet
from .models import Order
from django_filters import DateFilter


class OrderFilter(FilterSet):
    start_date = DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = DateFilter(field_name='created_at', lookup_expr='lte')
    class Meta:
        model = Order 
        fields = '__all__'
        exclude = ['customer', 'created_at']