from django.contrib import admin
from olxapp.models import Category, UserProfile, Product, Transaction

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Transaction)


# Register your models here.
