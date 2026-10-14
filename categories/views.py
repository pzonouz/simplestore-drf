from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer


class CategoryViewset(ModelViewSet):
    queryset = Category.objects.order_by("-created_at")
    serializer_class = CategorySerializer
