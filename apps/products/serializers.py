from rest_framework import serializers
from .models import Category, SubCategory, Product, Cart, CartItem, Wishlist
# ==================================
# CATEGORY SERIALIZER
# ==================================
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
# ==================================
# SUBCATEGORY SERIALIZER
# ==================================
class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name", read_only=True)
    class Meta:
        model = SubCategory
        fields = ["id", "subcategory_name", "category", "category_name"]
# ==================================
# PRODUCT SERIALIZER
# ==================================
class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category_name", read_only=True)
    subcategory_name = serializers.CharField(source="subcategory.subcategory_name", read_only=True)
    class Meta:
        model = Product
        fields = "__all__"
# ==================================
# CART ITEM SERIALIZER (Read Only)
# ==================================
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]
# ==================================
# CART SERIALIZER
# ==================================
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ["id", "user", "created_at", "items"]
# ==================================
# WISHLIST SERIALIZER
# ==================================
class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Wishlist
        fields = ["id", "user", "product"]