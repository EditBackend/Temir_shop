from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.name if self.name else "Nomsiz mahsulot"


class Sale(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='sales'
    )
    quantity = models.IntegerField()
    price = models.FloatField()
    total_price = models.FloatField()
    customer = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.total_price}"









