from django.urls import path
from .views import (
    CategoryListView,
    SubCategoryListView,
    ProductListView,
    ProductDetailView,
    AddToCartView,
    CartView,
    RemoveCartItemView,
    AddWishlistView,
    WishlistView
)

urlpatterns = [
    path("categories/", CategoryListView.as_view()),
    path("subcategories/", SubCategoryListView.as_view()),
    path("products/", ProductListView.as_view()),
    path("products/<int:id>/", ProductDetailView.as_view()),

    # CART
    path("cart/add/", AddToCartView.as_view()),
    path("cart/", CartView.as_view()),
    path("cart/remove/<int:id>/", RemoveCartItemView.as_view()),

    # WISHLIST
    path("wishlist/add/", AddWishlistView.as_view()),
    path("wishlist/", WishlistView.as_view()),
]
