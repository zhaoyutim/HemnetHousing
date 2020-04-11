from django.db import models


class HousingStatus(models.Model):
    address = models.Field(max_length=150)
    price = models.Field(max_length=150)
    area = models.Field(max_length=150)

    class Meta:
        verbose_name = "Author Yu Zhao"