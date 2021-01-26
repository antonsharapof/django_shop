from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import Category, Product, CategoryProduct, Cart
#
router = routers.SimpleRouter()
router.register(r'category', Category, basename="category")
router.register(r'product', Product, basename='product')
router.register(r'category/<int:category>', CategoryProduct, basename='category-product')
router.register(r'cart', Cart, basename='cart')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth', include('djoser.urls')),
    path('auth/token', obtain_auth_token, name='token'),
    path(r'', include(router.urls)),
]

