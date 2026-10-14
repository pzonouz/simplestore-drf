from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category


class CategorySerializer(ModelSerializer):
    parent_name = serializers.CharField(
        source="parent.name", read_only=True, default=None
    )

    class Meta:
        model = Category
        fields = ["id", "name", "parent", "parent_name", "description"]
