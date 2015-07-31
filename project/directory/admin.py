from django.contrib import admin
from directory.models import Product, Category


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
admin.site.register(Category, CategoryAdmin)