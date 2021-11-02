from django.urls import path, include

from products import views

urlpatterns = [
    path('products/', views.IndustryList.as_view()),
    path('industry/', views.ProductList.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]