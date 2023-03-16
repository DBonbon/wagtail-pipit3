from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField

from .base import BasePage


class ArticlePage(HeadlessPreviewMixin, BasePage):
    rich_text = RichTextField(blank=True, null=True, verbose_name=_("Rich text"))
    image = models.ForeignKey(
        "customimage.CustomImage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_(
            "If you want to override the image used on Facebook for"
        ),
        related_name="+",
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("rich_text"),
        FieldPanel("image"),
    ]

    """api_fields = [
        APIField('image'),
    ]"""

    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.ArticlePageSerializer"

    objects: PageManager

    class Meta:
        verbose_name = _("Article")
