from django.urls import path, include
from rest_framework import routers

from .views import Category, Product
#
router = routers.SimpleRouter()
router.register(r'category', Category, basename="Category")
router.register(r'product', Product, basename='product')

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', include(router.urls)),
]

