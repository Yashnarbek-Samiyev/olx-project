
from django.db import models
from django.contrib.auth.models import User
from modeltranslation.translator import TranslationOptions, register


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pics/', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Transaction(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='buyer_transactions')
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='seller_transactions')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Transaction #{self.id}'
