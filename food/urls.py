from django.urls import path
from .views import SearchProduct


urlpatterns = [
    path('search/',SearchProduct.as_view(),name='search_product'),
]