from .base_page import BasePageFactory
from ..pages.productlist import ProductListPage


class ProductListPageFactory(BasePageFactory):
    class Meta:
        model = ProductListPage
