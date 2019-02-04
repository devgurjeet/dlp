from django.contrib import admin

from .models import Plant, Product, PlanningData, HeadCount

admin.site.site_header = 'DLP administration'


class PlantViewAdmin(admin.ModelAdmin):
    list_display = ['plant_id', 'plant_name']
    # search_fields = ['title']


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ['plant_id', 'product_name']
    # search_fields = ['title']


class PlanningDataViewAdmin(admin.ModelAdmin):
    list_display = ['plant_id', 'fg_description', 'FG_code', 'DT_hrs', 'month', 'yearly_product_quantity', 'dt_value']

    def plant_id(self, instance):
        return instance.product_id.plant_id

    def fg_description(self, instance):
        return instance.product_id


class HeadCountViewAdmin(admin.ModelAdmin):
    list_display = ['plant_id', 'plant_family', 'month', 'ker', 'quantity']

    def plant_id(self, instance):
        return instance.product_id.plant_id

    def plant_family(self, instance):
        return instance.product_id


admin.site.register(Plant, PlantViewAdmin)
admin.site.register(Product)
admin.site.register(PlanningData, PlanningDataViewAdmin)
admin.site.register(HeadCount, HeadCountViewAdmin)
