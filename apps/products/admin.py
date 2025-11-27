from django.contrib import admin
from .models import Category, SubCategory, Product, Cart, CartItem, Wishlist

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Wishlist)