from django.urls import path
from .views import BasicProductDetail, BasicProductList

urlpatterns = [
    path("products/<int:pk>/",BasicProductDetail.as_view(), name='basic_product_detail'),
    path("products/",BasicProductList.as_view(),name="basic_product_list"),
]