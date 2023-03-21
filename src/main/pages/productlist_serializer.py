# main/pages/product_list_serializer.py
from .base_serializer import BasePageSerializer
from . import ProductListPage
from .article_serializer import ArticlePageSerializer
from rest_framework import serializers


class ProductListPageSerializer(BasePageSerializer):
    class Meta:
        model = ProductListPage
        fields = BasePageSerializer.Meta.fields


class ProductListDetailSerializer(ProductListPageSerializer):
    article = serializers.SerializerMethodField()

    class Meta:
        model = ProductListPage
        fields = ProductListPageSerializer.Meta.fields + [
            "article",
        ]

    def get_product(self, _page):
        article = self.context["article"]
        return ArticlePageSerializer(article).data




"""
class ProductListPageSerializer(BasePageSerializer):
    class Meta:
        model = ProductListPage
        fields = BasePageSerializer.Meta.fields

# main/pages/product_list_serializer.py
...
from example_app.serializer import ProductSerializer  # You will need to create this
...

class ProductListDetailSerializer(ProductListPageSerializer):
    article = serializers.SerializerMethodField()

    class Meta:
        model = ProductListPage
        fields = ProductListPageSerializer.Meta.fields + [
            "product",
        ]

    def get_product(self, _page):
        article = self.context.get("article")
        return ProductSerializer(article).data
"""
