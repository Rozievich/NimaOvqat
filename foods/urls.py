from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CategoryViewSet, SubCategoryViewSet, FoodViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")
router.register("category", CategoryViewSet, basename="categories")
router.register("subcategory", SubCategoryViewSet, basename="subcategories")
router.register("foods", FoodViewSet, basename="foods")

urlpatterns = [
    path('', include(router.urls))
]
