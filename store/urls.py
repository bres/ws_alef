from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
   path('', views.product_list, name='product_list'),
   # path('create-product/',views.create_product,name="create_product"),
   # path('update-product/<slug:slug>/',views.update_product,name="update_product"),
   # path('delete-product/<slug:slug>/',views.delete_product,name="delete_product"),
    path('category/<slug:category_slug>/', views.product_list,name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/',views.search,name='search'),
]
