from django.contrib import admin

from goods.models import Categories, Product
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount',]
    search_fields = ['name', 'description']
    list_filter = ['quantity', 'discount']

