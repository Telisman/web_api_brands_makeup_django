from django.db import models

class Brands(models.Model):
    name = models.CharField(max_length=100, default="None")
    price = models.DecimalField(max_digits=13,default=0,decimal_places=2,null=True)
    image_link = models.CharField( max_length=50, blank = True, null = True)
    brand = models.CharField( max_length=150, blank = True, null = True)
    category = models.CharField( max_length=150, blank = True, null = True)
    product_type = models.CharField( max_length=150, blank = True, null = True)
    description = models.CharField( max_length=1500, blank = True, null = True)

    def __str__(self):
        return self.name