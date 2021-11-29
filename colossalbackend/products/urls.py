from django.urls import path, include

from products import views

urlpatterns = [
    path('industry/', views.ProductList.as_view()),
    path('industries/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]