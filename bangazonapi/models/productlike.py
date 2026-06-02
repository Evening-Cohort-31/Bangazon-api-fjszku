from django.db import models
from .customer import Customer


class ProductLike(models.Model):

    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, related_name="likes"
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
