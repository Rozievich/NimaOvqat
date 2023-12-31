from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer, CategoryModelSerializer, SubCategoryModelSerializer, FoodModelSerializer
from django_filters import rest_framework as filters
from .models import User, Category, SubCategory, Food
from .permissions import IsSuperUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsSuperUser, )

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsSuperUser, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title', )


class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryModelSerializer
    permission_classes = (IsSuperUser, )
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title', 'category')

class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer
    permission_classes = (IsSuperUser, )
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = ('name', 'category')