# serializers.py

from rest_framework import serializers
from .models import Category, UserProfile, Product, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()  # Nested serializer for the owner
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    buyer = UserProfileSerializer()
    seller = UserProfileSerializer()
    product = ProductSerializer()

    class Meta:
        model = Transaction
        fields = '__all__'
