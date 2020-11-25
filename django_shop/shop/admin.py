from django.contrib import admin
from .models import Category, Product, Gallery
# Register your models here.
class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)