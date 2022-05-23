from django.urls import path
from .views import BaseProductDetail, BaseProductList

urlpatterns = [
    path("products/<int:pk>/",BaseProductDetail.as_view(), name='basic_product_detail'),
    path("products/",BaseProductList.as_view(),name="basic_product_list"),
]