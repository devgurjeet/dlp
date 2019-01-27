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
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    FG_code = models.CharField(max_length=500)
    DT_hrs = models.DecimalField(max_digits=5, decimal_places=2)


class HeadCount(models.Model):
    ker = models.DecimalField(max_digits=5, decimal_places=2)
    no_of_working_days = models.DecimalField(max_digits=5, decimal_places=2)
    working_hours_per_day = models.DecimalField(max_digits=5, decimal_places=2)
    testing_people = models.DecimalField(max_digits=5, decimal_places=2)








