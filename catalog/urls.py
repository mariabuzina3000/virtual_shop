from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, contacts, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/product_update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
]