from django.urls import path, include

from industries import views

urlpatterns = [
    path('products/', views.ProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]