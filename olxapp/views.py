# views.py

from rest_framework import generics, permissions, status, serializers
from rest_framework.response import Response
from .models import Category, UserProfile, Product, Transaction
from .serializers import (
    CategorySerializer,
    UserProfileSerializer,
    ProductSerializer,
    TransactionSerializer
)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.get(user=self.request.user)
        if not user_profile.is_premium_member:
            raise serializers.ValidationError(
                {'detail': 'Only premium members can create products.'})
        serializer.save(owner=self.request.user)

        if serializer.validated_data.get('price', 0) <= 0:
            raise serializers.ValidationError(
                {'price': 'Price must be greater than 0.'})

        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):

        if reached_max_products(request.user):
            return Response({'error': 'You have reached the maximum number of products you can create.'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


def reached_max_products(user):
    max_products_allowed = 5
    return Product.objects.filter(owner=user).count() >= max_products_allowed


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetail(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
