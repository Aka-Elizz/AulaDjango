from django.contrib import admin

from produtos.models import Category, Product, Brand, Color, Size

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'color', 'brand', 'price', 'stock','status',)
    list_editable = ('status', 'stock')
    save_as = True
    #comando para poder clicar no nome e modificar o produto
    list_display_links = ('id', 'name')
    search_fields = ("name", "id",)
    list_filter = ("size", "color")
    list_per_page = 10



admin.site.register(Product, ProductAdmin)


# Register your models here.
