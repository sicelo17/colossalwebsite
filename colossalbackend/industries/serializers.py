from rest_framework import serializers

from .models import Category, Industry
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail",
            "icon"
        )


class CategorySerializer(serializers.ModelSerializer):
    industry = IndustrySerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )