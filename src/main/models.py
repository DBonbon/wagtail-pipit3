from .pages import *  # NOQA: F403
from django.utils.translation import gettext_lazy as _
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.api import APIField
from wagtail.snippets.models import register_snippet
"""
class PostPageCategory(models.Model):
    page = ParentalKey(
        "pages.GamePage", on_delete=models.CASCADE, related_name="categories"
    )
    game_category = models.ForeignKey(
        "main.Category", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("category"),
    ]

    @property
    def category_name(self):
        return self.game_category.name

    api_fields = [
        APIField("category"),
        APIField("category_name"),
    ]

    class Meta:
        unique_together = ("page", "category")

@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


"""
