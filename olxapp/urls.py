
from django.urls import path
from .views import CategoryList, UserProfileDetail, ProductList, ProductDetail, TransactionList, TransactionDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('user-profiles/<int:pk>/', UserProfileDetail.as_view(),
         name='user-profile-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('transactions/', TransactionList.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(),
         name='transaction-detail'),
]
