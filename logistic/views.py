from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer, StockFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import api_view


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title',]
    search_fields = ['description', 'title']


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StockFilter
    search_fields = ['address', 'positions_product_id',]


@api_view(['GET'])
def sample_view(request):
    return Response({'message': 'ПРИВЕТ ceeeb!!!!!'})
