from django.urls import path
from .views import (product_detail_view,
                            product_create_view,
                            render_initial_data,
                            product_delete_view,
                            dynamic_lookup_view,
                            product_list_view)

app_name = 'products'

urlpatterns = [

    path('', product_list_view, name='product-list'),
    path('create/', product_create_view, name='product-create'),
    # Watch out : refer to ID if in product dynamic_lookup_view, it refers to ID
    path('<int:id>/', dynamic_lookup_view, name='product-detail'), # Based on product details view
    path('<int:product_id>/delete', product_delete_view, name='product-delete'),
    #path('product/', product_detail_view),


]
