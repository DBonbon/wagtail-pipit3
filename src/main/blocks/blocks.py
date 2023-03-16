from django import forms
from wagtail.core.blocks import (
    BooleanBlock,
    CharBlock,
    ChoiceBlock,
    DateTimeBlock,
    FieldBlock,
    IntegerBlock,
    ListBlock,
    PageChooserBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    StructValue,
    TextBlock,
    URLBlock,
)
from wagtail.core.blocks import RichTextBlock
from wagtail.rich_text import expand_db_html
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.conf import settings
from typing import Any, Dict, Optional
#from main.fields.fields import ImageRenditionField

class CustomRichTextBlock(RichTextBlock):
    def get_api_representation(self, value, context=None):
        return expand_db_html(value.source)


from wagtail.images.blocks import ImageChooserBlock

from main.fields.fields import ImageRenditionField
#from wagtail.images.api.fields import ImageRenditionField
#from rest_framework.fields import Field

class CustomRichTextBlock(RichTextBlock):
    def get_api_representation(self, value, context=None):
        return expand_db_html(value.source)

class CustomImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        return ImageRenditionField(
            ["width-512", "width-1024", "width-1536"]
        ).to_representation(value)


SPEECH_TYPES = (
        ('verb', 'Verb'),
        ('noun', 'Noun'),
        ('adjective', 'Adjective'),
        ('adverb', 'Adverb'),
        ('pronoun', 'Pronoun'),
        ('preposition', 'Preposition'),
        ('conjunction', 'Conjunction'),
        ('interjection', 'Interjection'),
        ('determiner', 'Determiner'),
    )

class CardBlock(blocks.StructBlock):
    """Basic game block that contains exactly 4 cards"""
    image = CustomImageChooserBlock(required=False, null=True, blank=True, label="image",)
    card_title = CharBlock(label="Card Title")
    card_subtitle = CharBlock(label="Card Subtitle", required=False, help_text="another text string can be used as hint, En translation, etc'")

    """class Meta:
        template = 'cms/card_block.html'
        icon = 'list-ol'"""

class GameBlock(blocks.StreamBlock):
    """Game unit which contains a un/limited niumber of 4 card units."""
    series = CardBlock(required=False, null=True, blank=True, label="image")
    title = CharBlock(label="Game Title")
    intro = CharBlock(label="Card Subtitle", required=False, help_text="describe the goal and/or add BG information, optional")


class ButtonBlock(blocks.StructBlock):
    button_text = blocks.CharBlock(required=True, max_length=50, label="Text")
    button_link = blocks.CharBlock(required=True, max_length=255, label="Link")


class TextAndButtonsBlock(blocks.StructBlock):
    text = blocks.TextBlock()
    buttons = blocks.ListBlock(ButtonBlock())
    mainbutton = ButtonBlock()

""""
card group min max 4 elements

each group is 4 cards

card - image, name, translation


"""
