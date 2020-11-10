from django.urls import path

from .views import (
    product_delete,
    product_create_view,
    product_detail_view, 
    render_initial_view,
    dynamic_lookup_view,
    product_list_view)
urlpatterns = [
    path('create/', product_create_view, name='create'),
    path('product/<int:my_id>/', dynamic_lookup_view, name='dynamic'),
    path('product/', product_detail_view, name='product'),
    path('edit/',render_initial_view, name='edit'),
    path('product/<int:my_id>/delete/', product_delete, name='product_delete'),
    path('list/',product_list_view, name='list'),
]