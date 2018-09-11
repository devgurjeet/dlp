from django.db import models


class Plant(models.Model):
    plant_id = models.CharField(max_length=100)
    plant_name = models.CharField(max_length=500)
    plant_detail = models.TextField(blank=True, null=True)


class Product(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    prooduct_family = models.CharField(max_length=500)
