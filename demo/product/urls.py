from django.urls import path
from . import views


urlpatterns = [
    path('', views.productOverview, name="product-overview"),
    path('item-list/', views.itemlist, name="item-list"),
    path('item-detail/<int:pk>/', views.itemDetail, name="item-detail"),
    path('item-create/', views.itemCreate, name="item-create"),
    path('item-update/<int:pk>/', views.itemUpdate, name="item-update"),
    path('item-delete/<int:pk>/', views.itemDelete, name="item-delete"),
    
]