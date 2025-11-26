from django.urls import path
from .views import CategoryListCreate, SubCategoryListCreate

urlpatterns = [
    path("category/", CategoryListCreate.as_view(), name="category"),
    path("subcategory/", SubCategoryListCreate.as_view(), name="subcategory"),
]