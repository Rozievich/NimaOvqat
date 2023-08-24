from rest_framework.serializers import ModelSerializer
from rest_framework.fields import ReadOnlyField
from .models import Category, SubCategory, User, Food


class UserModelSerializer(ModelSerializer):
    active = ReadOnlyField()

    class Meta:
        model = User
        fields = "telegram_id", "username", "first_name", "last_name", "active"


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SubCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = CategoryModelSerializer(instance.category).data
        return data


class FoodModelSerializer(ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = SubCategoryModelSerializer(instance.category).data
        return data
