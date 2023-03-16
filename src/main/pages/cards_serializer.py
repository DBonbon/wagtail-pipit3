from .base_serializer import BasePageSerializer
from . import CardsPage
from wagtail.rich_text import expand_db_html
from rest_framework import serializers
from main.fields.fields import ImageRenditionField


class CardsPageSerializer(BasePageSerializer):
    intro = serializers.SerializerMethodField()
    """body = StreamField(serializers={
        'quote': FirstQuoteSerializer,
        'image': ImageSerializer,
        'hero_section': HeroSectionSerializer
    })"""
    #image = ImageRenditionField()
    class Meta:
        model = CardsPage
        fields = BasePageSerializer.Meta.fields + [
            "intro",
            "cards",
            "card_title",
            "min_recommended_age",
            "max_recommended_age",
            "language",
        ]

    def get_intro(self, page):
        return expand_db_html(page.intro)
