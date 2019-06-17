from django.urls import path

from .views import SearchResultsView, autocomplete

urlpatterns = [
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('', SearchResultsView.as_view(), name='search_results'),
]