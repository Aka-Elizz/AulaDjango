from django.contrib import admin

from produtos.models import Category, Product, Brand, Color, Size

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'color', 'brand', 'price', 'stock','status')
    list_editable = ('status', 'stock')

admin.site.register(Product, ProductAdmin)


# Register your models here.
