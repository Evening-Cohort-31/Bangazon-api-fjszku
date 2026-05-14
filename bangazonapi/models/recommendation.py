from django.db import models
from .customer import Customer
from .product import Product


class Recommendation(models.Model):

    customer = models.ForeignKey(
        Customer,
        related_name="customer",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    recommender = models.ForeignKey(
        Customer,
        related_name="recommended_by",
        on_delete=models.CASCADE,
    )
