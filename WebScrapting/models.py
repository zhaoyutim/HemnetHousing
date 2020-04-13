from django.db import models


class HousingStatus(models.Model):
    address = models.TextField(max_length=150)
    price = models.TextField(max_length=150)
    area = models.TextField(max_length=150)

    class Meta:
        verbose_name = "Author Yu Zhao"