from django.db import models
import uuid


class Product(models.Model):
    product_id = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True, null=False)
    product_name = models.CharField(max_length=200, default=None)
    product_description = models.TextField(null=True, blank=True)
    product_seller = models.CharField(max_length=200, null=True, blank=True)
    product_date = models.DateTimeField(auto_now_add=True)
    product_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.product_name


class Cart(models.Model):
    cart_id = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True, null=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_id.product_name
