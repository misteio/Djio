from .serializers import CategoryTreeSerializer
from rest_framework.generics import (ListAPIView)
from ..models import Category


class CategoryAPIListView(ListAPIView):
    queryset = Category.objects.all().filter(level__lte=0)
    serializer_class = CategoryTreeSerializer
