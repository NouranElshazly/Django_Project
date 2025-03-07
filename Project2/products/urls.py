from django import views
from .views import  *
from django.urls import path
from django.urls import path
 
urlpatterns = [
    path("products/", AllProductsView.as_view(), name="all_products"),
    path("" ,Home_page, name="home"),
    path("<int:pk>/", ProductDetailView.as_view(), name="one_product"),
    path("products/category/", AllCategoriesView.as_view(), name="all_categ"),
    path("products/category/<int:category_id>/", CategoryProductsView.as_view(), name="one_category"),
 
    path("products/category/add/", AddCategoryView.as_view(), name="add_category"),
    path("product/add/", AddProductView.as_view(), name="add_product"),
    path("product/edit/<int:pk>" ,EditProductView.as_view() ,name="edit_product"),
    path("products/category/edit/<int:pk>" ,EditCategoryView.as_view() , name = "edit_category"),
    path("product/delete/<int:pk>/", DeleteProductView.as_view(), name="delete_product"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',  remove_from_cart, name='remove_from_cart'),
    path('cart/',  cart_detail, name='cart_detail'),
 
  
  
   
 ]
