from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django_filters.rest_framework import CharFilter, FilterSet
from django.db.models import F

from .models import Wine


class WineFilterSet(FilterSet):
    query = CharFilter(method='filter_query')

    def filter_query(self, queryset, name, value):
        return queryset.annotate(
            search_vector=(
                SearchVector('variety', weight='A') +
                SearchVector('winery', weight='A') +
                SearchVector('description', weight='B')
            ),
            search_rank=SearchRank(F('search_vector'), SearchQuery(value))
        ).filter(
            search_vector=SearchQuery(value)
        ).order_by('-search_rank', 'id')

    class Meta:
        model = Wine
        fields = ('query', 'country', 'points',)
