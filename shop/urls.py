from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
   path('', views.product_list, name='product_list'),
   path('create-product/',views.create_product,name="create_product"),
   path('update-product/<slug:slug>/',views.update_product,name="update_product"),
   path('delete-product/<slug:slug>/',views.delete_product,name="delete_product"),
   path('<slug:category_slug>/', views.product_list,
        name='product_list_by_category'),
   path('<int:id>/<slug:slug>/', views.product_detail,
        name='product_detail'),
]