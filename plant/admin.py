from django.contrib import admin

from .models import Plant, Product


class PlantViewAdmin(admin.ModelAdmin):
    list_display = ['plant_id', 'plant_name']
    # search_fields = ['title']


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ['plant_id', 'product_name']
    # search_fields = ['title']


admin.site.register(Plant, PlantViewAdmin)
admin.site.register(Product)
