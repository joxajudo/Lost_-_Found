from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.geocoders import Nominatim  # Install geopy if not already installed

from app.models import Category, Item, User, SubCategory
from app.permission import IsAuthorOrReadOnly
from app.serializers.other import CategorySerializer, ItemSerializer, UserSerializer, SubCategorySerializer


class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    parser_classes = [MultiPartParser, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['name', 'country', 'city']


class ItemViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthorOrReadOnly, ]
    parser_classes = [MultiPartParser, ]
    filter_backends = [SearchFilter, ]
    search_fields = ['name', 'country', 'city']


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
