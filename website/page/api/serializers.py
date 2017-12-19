from rest_framework import serializers
from ..models import Category


class CategoryTreeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    created_at = serializers.DateTimeField().to_representation
    status = serializers.CharField()
    slug = serializers.CharField()
    folder = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()

    def get_folder(self, obj):
        if obj.get_children():
            return True
        else:
            return False

    def get_key(self, obj):
        return obj.id

    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'children', 'status', 'slug', 'folder', 'key']

    def get_fields(self):
        fields = super().get_fields()
        fields['children'] = CategoryTreeSerializer(many=True)
        return fields
