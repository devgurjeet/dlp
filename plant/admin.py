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
    list_display = ['plant_id', 'FG_code', 'DT_hrs']


class HeadCountViewAdmin(admin.ModelAdmin):
    list_display = ['ker', 'no_of_working_days', 'working_hours_per_day', 'testing_people']


admin.site.register(Plant, PlantViewAdmin)
admin.site.register(Product)
admin.site.register(PlanningData)
admin.site.register(HeadCount)

