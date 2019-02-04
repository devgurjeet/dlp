from django.db import models
from django.db.models import Sum
from decimal import Decimal

DECIMAL_PLACES = 2

MONTH_CHOICES = (
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)


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
    class Meta:
        verbose_name_plural = 'Planning Data'

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    FG_code = models.CharField(max_length=500)
    DT_hrs = models.DecimalField(max_digits=20, decimal_places=2)
    month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    yearly_product_quantity = models.DecimalField(max_digits=20, decimal_places=2)

    @property
    def dt_value(self):
        return self.DT_hrs * self.yearly_product_quantity

    def __str__(self):
        return "{} | {}".format(self.product_id, self.FG_code)


class HeadCount(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    ker = models.DecimalField(max_digits=15, decimal_places=2)
    no_of_working_days = models.DecimalField(max_digits=15, decimal_places=2)
    working_hours_per_day = models.DecimalField(max_digits=15, decimal_places=2)
    testing_people = models.DecimalField(max_digits=15, decimal_places=2)

    @property
    def quantity(self):
        qty = PlanningData.objects.filter(month=self.month).aggregate(Sum('yearly_product_quantity'))
        return round(qty['yearly_product_quantity__sum'], DECIMAL_PLACES)

    @property
    def dt(self):
        dt_values = 0

        items = PlanningData.objects.filter(month=self.month)

        for item in items:
            dt_values += item.dt_value

        return round(dt_values, DECIMAL_PLACES)

    @property
    def otr(self):
        return round(self.dt / self.ker, DECIMAL_PLACES)

    @property
    def head_count(self):
        return round((self.otr / self.no_of_working_days / self.working_hours_per_day) - self.testing_people,
                     DECIMAL_PLACES)

    def __str__(self):
        return self.month
