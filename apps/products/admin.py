from django.contrib import admin
from .models import Category, SubCategory, Product, Cart, CartItem, Wishlist

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")
    search_fields = ("category_name",)


# admin.site.register(SubCategory)
@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "subcategory_name", "category")
    list_filter = ("category",)
    search_fields = ("subcategory_name",)

# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product_name", "category", "subcategory", "purity", "price", "stock")
    list_filter = ("category", "subcategory", "purity")
    search_fields = ("product_name", "sku")
    ordering = ("-created_at",)

# admin.site.register(Cart)
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    search_fields = ("user__username",)
    ordering = ("-created_at",)

# admin.site.register(CartItem)
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "product", "quantity")
    list_filter = ("product",)
    search_fields = ("product__product_name",)

# admin.site.register(Wishlist)
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "product")
    list_filter = ("user",)
    search_fields = ("user__username", "product__product_name")