from rest_framework import serializers
from wagtail.rich_text import expand_db_html

from .base_serializer import BasePageSerializer
from . import ArticlePage
from main.fields.fields import ImageRenditionField

class ArticlePageSerializer(BasePageSerializer):
    rich_text = serializers.SerializerMethodField()
    image = ImageRenditionField()

    class Meta:
        model = ArticlePage
        fields = BasePageSerializer.Meta.fields + ["rich_text", "image",]

    def get_rich_text(self, page):
        return expand_db_html(page.rich_text)
