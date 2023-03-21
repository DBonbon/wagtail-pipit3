from django.utils.translation import gettext_lazy as _
from wagtail.models import PageManager
from wagtail_headless_preview.models import HeadlessPreviewMixin
from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework.response import Response
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail_headless_preview.models import HeadlessPreviewMixin
from django.http import HttpResponse, JsonResponse
from .base import BasePage
from .article import ArticlePage as Article

class ProductListPage(HeadlessPreviewMixin, RoutablePageMixin, BasePage):
    extra_panels = BasePage.extra_panels
    serializer_class = "main.pages.ProductListPageSerializer"
    #serializer_class = "main.pages.ProductListSerializer"

    objects: PageManager

    class Meta:
        verbose_name = _("ProductList")

    @route(r'^$')
    def index_route(self, request, *args, **kwargs):
        data = self.get_component_data({"request": request})
        # Decide response depending if called through api or wagtail routing
        response_cls = Response if isinstance(request, Request) else JsonResponse
        return response_cls(data)

    @route(r'^articles/(?P<slug>.+)/$')
    def product_detail(self, request, slug=None, *args, **kwargs):
        article = get_object_or_404(Article, slug=slug)

        context = {"request": request, "article": article}
        data = self.get_component_data(
            context=context,
            component_name="Article",
            serializer_cls="main.pages.ArticleSerializer",
        )

        # Decide response depending if called through api or wagtail routing
        response_cls = Response if isinstance(request, Request) else JsonResponse
        return response_cls(data)
