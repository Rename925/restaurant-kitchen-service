from django.contrib.auth.models import AbstractUser
from django.db import models

from restaurant import settings


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dish")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL,  related_name="dish", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} cost {self.price} ({self.description})"


class Cook(AbstractUser):

    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"
