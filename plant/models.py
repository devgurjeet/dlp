from django.db import models


class Plant(models.Model):
    plant_id = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=500)
    plant_detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.plant_id


class Product(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    product_family = models.CharField(max_length=500)

    def __str__(self):
        return self.product_family


class PlanningData(models.Model):
    pass







