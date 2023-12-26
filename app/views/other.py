from rest_framework import viewsets, generics, filters
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView, \
    UpdateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from geopy.geocoders import Nominatim  # Install geopy if not already installed
from unicodedata import category

from app.models import Category, Item, User, SubCategory, About, AboutCategory, NewsLetter, UserProfile
from app.permission import IsAuthorOrReadOnly
from app.serializers.other import CategorySerializer, ItemSerializer, UserSerializer, SubCategorySerializer, \
    AboutSerializer, AboutCategorySerializer, UserModelSerializer, NewsLetterSerializer, UserProfileSerializer, \
    UserUpdateSerializer


class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class SubCategoryViewSet(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class AboutCategoryViewSet(ListAPIView):
    queryset = AboutCategory.objects.all()
    serializer_class = AboutCategorySerializer


class AboutViewSet(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


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


class ItembyCategoryAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        category = self.kwargs['category_id']
        return Item.objects.filter(category=category).all()


class ItembyUserAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        user = self.kwargs['user_id']
        return Item.objects.filter(user=user).all()


class ItembyRequestUserView(generics.ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'type', 'category__name']

    def get_queryset(self):
        # Retrieve the current user.
        user = self.request.user
        # Filter the items by the current user.
        queryset = Item.objects.filter(user=user)

        # Retrieve query parameters for additional filtering.
        category = self.request.query_params.get('category', None)
        name = self.request.query_params.get('name', None)
        item_type = self.request.query_params.get('type', None)

        # Apply filters based on the presence of query parameters.
        if category:
            queryset = queryset.filter(category__name=category)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if item_type:
            queryset = queryset.filter(type=item_type)

        return queryset


class ItembyTypeAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        type = self.kwargs['type']
        return Item.objects.filter(type=type).all()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserModelSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsLetterViewSet(CreateAPIView):
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer
    permission_classes = [IsAuthenticated]


# class UserProfileListCreateView(generics.ListCreateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser]
#
#
# class UserProfileDetailView(UpdateAPIView):
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer
#     permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser]


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def get_object(self):
        return self.request.user