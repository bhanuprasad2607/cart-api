from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.productPage, name="list_products"),
    path('add-product/', views.addProduct, name='add_product'),
    path('add-product/<str:id>', views.updateProduct, name='update_product'),
    path('products/<str:id>/', views.deleteProduct, name="delete_product"),

    path('cart/add/<str:id>', views.addCart, name="add_cart"),
    path('cart/', views.cartPage, name="list_cart"),
    path('cart/delete/<str:id>/', views.delProductCart, name="del_product_cart"),

    path('api/product/', views.product, name="api_list_products"),
    path('api/product/<str:id>/', views.product_view, name="api_product_view"),
    path('api/cart/', views.cartApi, name="api_list_cart")
]
